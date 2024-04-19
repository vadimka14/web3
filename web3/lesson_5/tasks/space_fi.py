import time
import asyncio
import random

from web3 import Web3
from web3.types import TxParams

from tasks.base import Base
from eth_async.models import RawContract, TxArgs, TokenAmount
from data.models import Contracts


# SpaceFiABI = [
#     {
#         'constant': False,
#         'inputs': [
#             {'name': 'amountOut', 'type': 'uint256'},
#             {'name': 'path', 'type': 'address[]'},
#             {'name': 'toAddress', 'type': 'address'},
#             {'name': 'deadline', 'type': 'uint256'},
#         ],
#         'name': 'no_name',
#         'outputs': [],
#         'payable': False,
#         'stateMutability': 'nonpayable',
#         'type': 'function'
#     },
# ]

class SpaceFi(Base):
    async def _swap(
            self,
            path=list[str],
            amount: TokenAmount | None = None,
            slippage: float = 1.,
    ) -> str:
        from_token_address = Web3.to_checksum_address(path[0])
        to_token_address = Web3.to_checksum_address(path[-1])

        from_token_is_eth = from_token_address.upper() == Contracts.WETH.address.upper()

        from_token = await self.client.contracts.default_token(contract_address=from_token_address)
        from_token_name = await from_token.functions.symbol().call()
        #виправить
        if from_token_name == 'WETH':
            from_token_name = 'ETH'
        if from_token_name == 'WBTC':
            from_token_name = 'BTC'
        if from_token_name == 'ceBUSD':
            from_token_name = 'BUSD'
        if from_token_name == 'USDC.e':
            from_token_name = 'USDC'

        to_token = await self.client.contracts.default_token(contract_address=to_token_address)
        to_token_name = await to_token.functions.symbol().call()
        if to_token_name == 'WETH':
            to_token_name = 'ETH'
        if to_token_name == 'WBTC':
            to_token_name = 'BTC'
        if to_token_name == 'ceBUSD':
            to_token_name = 'BUSD'
        if to_token_name == 'USDC.e':
            to_token_name = 'USDC'

        failed_text = f'Failed swap {from_token_name} to {to_token_name} via SpaceFi'

        contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)

        if not from_token_is_eth:
            if await self.approve_interface(
                    token_address=from_token.address,
                    spender=contract.address,
                    amount=amount
            ):
                await asyncio.sleep(random.randint(5, 10))
            else:
                return f'{failed_text} | can not approve'

        if from_token_name in ('BUSD', 'USDT'):
            from_token_price_dollar = 1
        else:
            from_token_price_dollar = await self.get_token_price(token_symbol=from_token_name)

        if to_token_name in ('BUSD', 'USDT'):
            to_token_price_dollar = 1
        else:
            to_token_price_dollar = await self.get_token_price(token_symbol=to_token_name)

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * (from_token_price_dollar / to_token_price_dollar) * (100 - slippage) / 100,
            decimals=await self.client.transactions.get_decimals(contract=to_token_address)
            )

        if from_token_is_eth:
            '''
            0x7ff36ab5
0000000000000000000000000000000000000000000000000000000000056338 - amountOut
0000000000000000000000000000000000000000000000000000000000000080 - array link
0000000000000000000000007131b37478af63e775402248583099974a005b75 - address
000000000000000000000000000000000000000000000000000000006603f39e - deadline
0000000000000000000000000000000000000000000000000000000000000002 array size
0000000000000000000000005aea5775959fbc2557cc8789bc1bf90a239d9a91 - WETH
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC
            '''
            data = (f'0x7ff36ab5'
                    f'{self._get_swap_data(amount_out_min.Wei)}'
                    f'{"80".zfill(64)}'
                    f'{self._get_swap_data(self.client.account.address)}'
                    f'{self._get_swap_data(int(time.time() + 20 * 60))}'
                    f'{self._get_swap_data(len(path))}'
            )
            for p in path:
                data += p[2:].lower().zfill(64)

            # self.parse_params(params=data)
            # return

            # params = TxArgs(
            #     amountOut=amount_out_min.Wei,
            #     path=path,
            #     toAddress=self.client.account.address,
            #     deadline=int(time.time() + 20 * 60),
            # )
        else:
            '''0x18cbafe5
00000000000000000000000000000000000000000000000006f05b59d3b20000 - amountIn
00000000000000000000000000000000000000000000000000007ff865a6d378 - amountOut
00000000000000000000000000000000000000000000000000000000000000a0 - array link
0000000000000000000000007131b37478af63e775402248583099974a005b75 - address
0000000000000000000000000000000000000000000000000000000066045d26 - deadline
0000000000000000000000000000000000000000000000000000000000000002 - array size
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC
0000000000000000000000005aea5775959fbc2557cc8789bc1bf90a239d9a91 - WETH
'''
            data = (f'0x18cbafe5'
                    f'{self._get_swap_data(amount.Wei)}'
                    f'{self._get_swap_data(amount_out_min.Wei)}'
                    f'{"a0".zfill(64)}'
                    f'{self._get_swap_data(self.client.account.address)}'
                    f'{self._get_swap_data(int(time.time() + 20 * 60))}'
                    f'{self._get_swap_data(len(path))}'
            )
            for p in path:
                data += p[2:].lower().zfill(64)

            # self.parse_params(params=data)
            # return

            # params = TxArgs(
            #     amountIn=amount.Wei,
            #     amountOutMin=amount_out_min.Wei,
            #     path=path,
            #     to=self.client.account.address,
            #     deadline=int(time.time() + 20 * 60)
            # )

        function_name = 'swapExactETHForTokens' if from_token_is_eth \
            else 'swapExactTokensForETH'

        tx_params = TxParams(
            to=contract.address,
            data=data,  # contract.encodeABI(function_name, args=params.tuple())
            value=amount.Wei if from_token_is_eth else 0
        )

        # self.parse_params(params=tx_params['data'])
        # return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_usdc(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.WETH.address, Contracts.USDC.address],
            slippage=slippage
        )

    async def swap_usdc_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.USDC.address, Contracts.WETH.address],
            slippage=slippage
        )

    async def swap_eth_to_usdt(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.WETH.address, Contracts.USDT.address],
            slippage=slippage
        )

    async def swap_usdt_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.USDT.address, Contracts.WETH.address],
            slippage=slippage
        )

    async def swap_eth_to_busd(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.WETH.address, Contracts.ceBUSD.address],
            slippage=slippage
        )

    async def swap_busd_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.ceBUSD.address, Contracts.WETH.address],
            slippage=slippage
        )

    async def swap_eth_to_wbtc(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.WETH.address, Contracts.WBTC.address],
            slippage=slippage
        )

    async def swap_wbtc_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage=1.,
    ) -> str:
        return await self._swap(
            amount=amount,
            path=[Contracts.WBTC.address, Contracts.WETH.address],
            slippage=slippage
        )

    def _get_swap_data(
            self,
            data
    ) -> str:
        if data == self.client.account.address:
            return str(data).lower()[2:].zfill(64)
        else:
            return hex(data)[2:].zfill(64)

