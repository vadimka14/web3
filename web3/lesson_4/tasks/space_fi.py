import time
import asyncio
import random

from web3 import Web3
from web3.types import TxParams

from tasks.base import Base
from eth_async.models import RawContract, TxArgs, TokenAmount
from data.models import Contracts


SpaceFiABI = [
    {
        'constant': False,
        'inputs': [
            {'name': 'amountOut', 'type': 'uint256'},
            {'name': 'path', 'type': 'address[]'},
            {'name': 'toAddress', 'type': 'address'},
            {'name': 'deadline', 'type': 'uint256'},
        ],
        'name': 'no_name',
        'outputs': [],
        'payable': False,
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
]
# '''
# 0x7ff36ab5
# 000000000000000000000000000000000000000000000000000000000017d8be - amountOut
# 0000000000000000000000000000000000000000000000000000000000000080
# 000000000000000000000000e747990d5a3df6737851022cba3a32efe85684e7 - to address
# 0000000000000000000000000000000000000000000000000000000064ff27fd - deadline
# 0000000000000000000000000000000000000000000000000000000000000002
# 0000000000000000000000005aea5775959fbc2557cc8789bc1bf90a239d9a91 - WETH
# 0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC
#
# 0x00448adc
# 000000000000000000000000000000000000000000000000000000000033666a amountout
# 0000000000000000000000007131b37478af63e775402248583099974a005b75 address
# 0000000000000000000000000000000000000000000000000000000065ff1b58 deadline
# 0000000000000000000000000000000000000000000000000000000000000080
# 0000000000000000000000000000000000000000000000000000000000000002
# 0000000000000000000000005aea5775959fbc2557cc8789bc1bf90a239d9a91 weth
# 0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 usdc
# '''


class SpaceFi(Base):
    # router = RawContract(
    #     title='space_fi',
    #     address='0xbE7D1FD1f6748bbDefC4fbaCafBb11C6Fc506d1d',
    #     abi=SpaceFiABI
    # )
    #
    # async def swap_eth_to_usdc(
    #         self,
    #         amount: TokenAmount,
    #         slippage=1.,
    # ) -> str:
    #     to_token = Contracts.USDC
    #
    #     to_token = await self.client.contracts.default_token(contract_address=to_token.address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap ETH to {to_token_name} via SpaceFi'
    #
    #     contract = await self.client.contracts.get(contract_address=SpaceFi.router)
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
    #         decimals=await self.client.transactions.get_decimals(contract=to_token.address)
    #     )
    #
    #     params = TxArgs(
    #         amountOut=amount_out_min.Wei,
    #         path=[Contracts.WETH.address, Contracts.USDC.address],
    #         toAddress=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60),
    #     )
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('no_name', args=params.tuple()),
    #         value=amount.Wei
    #     )
    #
    #     data = tx_params['data']
    #     tx_params['data'] = '0x7ff36ab5' + data[10:]
    #
    #     # print(tx_params['data'])
    #     # return
    #     # шоб перевірить функцію на справність:
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_usdc_to_eth(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ) -> str:
    #     from_token = await self.client.contracts.default_token(contract_address=Contracts.USDC.address)
    #     from_token_name = await from_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap {from_token_name} to ETH via SpaceFi'
    #
    #     if not amount:
    #         amount = await self.client.wallet.balance(token=from_token)
    #         if not amount.Wei:
    #             return f'{failed_text}: {self.client.account.address} | Space_Fi | swap_token | ' \
    #                    f'not enough {from_token_name} balance ({amount.Ether})'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     if await self.approve_interface(
    #         token_address=from_token.address,
    #         spender=contract.address,
    #         amount=amount
    #     ):
    #         await asyncio.sleep((random.randint(5, 10)))
    #     else:
    #         return f'{failed_text} | can not approve'
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
    #         decimals=18
    #     )
    #
    #     params = TxArgs(
    #         amountIn=amount.Wei,
    #         amountOutMin=amount_out_min.Wei,
    #         path=[Contracts.USDC.address, Contracts.WETH.address],
    #         to=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60)
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactTokensForETH', args=params.tuple())
    #     )
    #
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} {from_token_name} was swapped to ETH via Space_Fi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    #
    # async def swap_eth_to_usdt(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ) -> str:
    #     to_token = Contracts.USDT
    #
    #     to_token = await self.client.contracts.default_token(contract_address=to_token.address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap ETH to {to_token_name} via SpaceFi'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
    #         decimals=await self.client.transactions.get_decimals(contract=to_token.address)
    #     )
    #
    #     params = TxArgs(
    #         amountOut=amount_out_min.Wei,
    #         path=[Contracts.WETH.address, Contracts.USDT.address],
    #         toAddress=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60),
    #     )
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactETHForTokens', args=params.tuple()),
    #         value=amount.Wei
    #     )
    #
    #     tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_usdt_to_eth(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ) -> str:
    #     from_token = await self.client.contracts.default_token(contract_address=Contracts.USDT.address)
    #     from_token_name = await from_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap {from_token_name} to ETH via SpaceFi'
    #
    #     if not amount:
    #         amount = await self.client.wallet.balance(token=from_token)
    #         if not amount.Wei:
    #             return f'{failed_text}: {self.client.account.address} | Space_Fi | swap_token | ' \
    #                    f'not enough {from_token_name} balance ({amount.Ether})'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     if await self.approve_interface(
    #             token_address=from_token.address,
    #             spender=contract.address,
    #             amount=amount
    #     ):
    #         await asyncio.sleep((random.randint(5, 10)))
    #     else:
    #         return f'{failed_text} | can not approve'
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) / eth_price * (1 - slippage / 100)
    #     )
    #
    #     params = TxArgs(
    #         amountIn=amount.Wei,
    #         amountOutMin=amount_out_min.Wei,
    #         path=[Contracts.USDT.address, Contracts.WETH.address],
    #         to=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60)
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactTokensForETH', args=params.tuple())
    #     )
    #
    #     tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_eth_to_busd(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ) -> str:
    #     to_token = Contracts.ceBUSD
    #
    #     to_token = await self.client.contracts.default_token(contract_address=to_token.address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap ETH to {to_token_name} via SpaceFi'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
    #         decimals=await self.client.transactions.get_decimals(contract=to_token.address)
    #     )
    #
    #     params = TxArgs(
    #         amountOut=amount_out_min.Wei,
    #         path=[Contracts.WETH.address, Contracts.ceBUSD.address],
    #         toAddress=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60),
    #     )
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactETHForTokens', args=params.tuple()),
    #         value=amount.Wei
    #     )
    #
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_busd_to_eth(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ):
    #     from_token = await self.client.contracts.default_token(contract_address=Contracts.ceBUSD.address)
    #     from_token_name = await from_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap {from_token_name} to ETH via SpaceFi'
    #
    #     if not amount:
    #         amount = await self.client.wallet.balance(token=from_token)
    #         if not amount.Wei:
    #             return f'{failed_text}: {self.client.account.address} | Space_Fi | swap_token | ' \
    #                    f'not enough {from_token_name} balance ({amount.Ether})'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     if await self.approve_interface(
    #             token_address=from_token.address,
    #             spender=contract.address,
    #             amount=amount
    #     ):
    #         await asyncio.sleep((random.randint(5, 10)))
    #     else:
    #         return f'{failed_text} | can not approve'
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) / eth_price * (1 - slippage / 100)
    #     )
    #
    #     params = TxArgs(
    #         amountIn=amount.Wei,
    #         amountOutMin=amount_out_min.Wei,
    #         path=[Contracts.ceBUSD.address, Contracts.WETH.address],
    #         to=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60)
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactTokensForETH', args=params.tuple())
    #     )
    #
    #     tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_eth_to_wbtc(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ):
    #     to_token = Contracts.WBTC
    #
    #     to_token = await self.client.contracts.default_token(contract_address=to_token.address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap ETH to {to_token_name} via SpaceFi'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #     wbtc_price = await self.get_token_price(token_symbol='BTC')
    #
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * eth_price / wbtc_price * (1 - slippage / 100),
    #         decimals=await self.client.transactions.get_decimals(contract=to_token.address)
    #     )
    #
    #     params = TxArgs(
    #         amountOut=amount_out_min.Wei,
    #         path=[Contracts.WETH.address, Contracts.WBTC.address],
    #         toAddress=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60),
    #     )
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactETHForTokens', args=params.tuple()),
    #         value=amount.Wei
    #     )
    #
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'
    #
    # async def swap_wbtc_to_eth(
    #         self,
    #         amount: TokenAmount | None = None,
    #         slippage: float = 1.,
    # ) -> str:
    #     from_token = await self.client.contracts.default_token(contract_address=Contracts.WBTC.address)
    #     from_token_name = await from_token.functions.symbol().call()
    #
    #     failed_text = f'Failed swap {from_token_name} to ETH via Mute'
    #
    #     if not amount:
    #         amount = await self.client.wallet.balance(token=from_token)
    #         if not amount.Wei:
    #             return f'{failed_text}: {self.client.account.address} | Space_Fi | swap_token | ' \
    #                    f'not enough {from_token_name} balance ({amount.Ether})'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.SPACE_FI)
    #
    #     if await self.approve_interface(
    #             token_address=from_token.address,
    #             spender=contract.address,
    #             amount=amount
    #     ):
    #         await asyncio.sleep(random.randint(5, 10))
    #     else:
    #         return f'{failed_text} | can not approve'
    #
    #     wbtc_price = await self.get_token_price(token_symbol='BTC')
    #     eth_price = await self.get_token_price(token_symbol='ETH')
    #
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * (wbtc_price / eth_price) * (1 - slippage / 100),
    #     )
    #
    #     params = TxArgs(
    #         amountIn=amount.Wei,
    #         amountOutMin=amount_out_min.Wei,
    #         path=[Contracts.WBTC.address, Contracts.WETH.address],
    #         to=self.client.account.address,
    #         deadline=int(time.time() + 20 * 60)
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=contract.encodeABI('swapExactTokensForETH', args=params.tuple())
    #     )
    #
    #     tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} ETH was swapped to {to_token_name} via SpaceFi: {tx.hash.hex()}'
    #     return f'{failed_text}!'

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

        to_token = await self.client.contracts.default_token(contract_address=to_token_address)
        to_token_name = await to_token.functions.symbol().call()
        if to_token_name == 'WETH':
            to_token_name = 'ETH'
        if to_token_name == 'WBTC':
            to_token_name = 'BTC'
        if to_token_name == 'ceBUSD':
            to_token_name = 'BUSD'

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

        from_token_price_dollar = await self.get_token_price(token_symbol=from_token_name)
        to_token_price_dollar = await self.get_token_price(token_symbol=to_token_name)

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * from_token_price_dollar / to_token_price_dollar * (100 - slippage) / 100,
            decimals=await self.client.transactions.get_decimals(contract=to_token_address)
            )

        if from_token_is_eth:
            params = TxArgs(
                amountOut=amount_out_min.Wei,
                path=path,
                toAddress=self.client.account.address,
                deadline=int(time.time() + 20 * 60),
            )
        else:
            params = TxArgs(
                amountIn=amount.Wei,
                amountOutMin=amount_out_min.Wei,
                path=path,
                to=self.client.account.address,
                deadline=int(time.time() + 20 * 60)
            )

        function_name = 'swapExactETHForTokens' if from_token_is_eth \
            else 'swapExactTokensForETH'

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI(function_name, args=params.tuple()),
            value=amount.Wei if from_token_is_eth else 0
        )

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via Mute: {tx.hash.hex()}'
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





