import asyncio
import random
import logging
import time

from web3 import Web3
from eth_async.models import RawContract, TokenAmount
from web3.types import TxParams, HexStr

from tasks.base import Base
from data.models import Contracts


class Maverick(Base):
    PATH_MAP_BUY = {
        'USDC.e': [
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
            Web3.to_bytes(hexstr=HexStr('41c8cf74c27554a8972d3bf3d2bd4a14d8b604ab')),
            Web3.to_bytes(hexstr=HexStr(Contracts.USDC.address)),
        ],
        'BUSD': [
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
            Web3.to_bytes(hexstr=HexStr('3ae63fb198652e294b8de4c2ef659d95d5ff28be')),
            Web3.to_bytes(hexstr=HexStr(Contracts.ceBUSD.address)),
        ],
        'USDT': [
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
            Web3.to_bytes(hexstr=HexStr('c0622acb4e15744a83ecb64f661b1a119e2d11bf')),
            Web3.to_bytes(hexstr=HexStr(Contracts.USDT.address)),
        ]
    }
    PATH_MAP_SELL = {
        'USDC.e': [
            Web3.to_bytes(hexstr=HexStr(Contracts.USDC.address)),
            Web3.to_bytes(hexstr=HexStr('688ea0d07acadd7d74ec7c729f1d0ca0dd4bb665')),
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
        ],
        'BUSD': [
            Web3.to_bytes(hexstr=HexStr(Contracts.ceBUSD.address)),
            Web3.to_bytes(hexstr=HexStr('3ae63fb198652e294b8de4c2ef659d95d5ff28be')),
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
        ],
        'USDT': [
            Web3.to_bytes(hexstr=HexStr(Contracts.USDT.address)),
            Web3.to_bytes(hexstr=HexStr('c0622acb4e15744a83ecb64f661b1a119e2d11bf')),
            Web3.to_bytes(hexstr=HexStr(Contracts.WETH.address)),
        ]
    }

    # async def _swap_eth_to_token(
    #         self,
    #         amount: TokenAmount,
    #         to_token: RawContract,
    #         slippage: float = 1.0
    # ) -> str:
    #     to_token_address = Web3.to_checksum_address(to_token.address)
    #     to_token = await self.client.contracts.default_token(contract_address=to_token_address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     path = self.PATH_MAP_BUY[to_token_name]
    #
    #     from_token_address = Web3.to_checksum_address(path[0])
    #     from_token = await self.client.contracts.default_token(contract_address=from_token_address)
    #     from_token_name = await from_token.functions.symbol().call()
    #     if from_token_name == 'WETH':
    #         from_token_name = 'ETH'
    #     if from_token_name == 'WBTC':
    #         from_token_name = 'BTC'
    #     if from_token_name == 'ceBUSD':
    #         from_token_name = 'BUSD'
    #     if from_token_name == 'USDC.e':
    #         from_token_name = 'USDC'
    #
    #     if to_token_name == 'WETH':
    #         to_token_name = 'ETH'
    #     if to_token_name == 'WBTC':
    #         to_token_name = 'BTC'
    #     if to_token_name == 'ceBUSD':
    #         to_token_name = 'BUSD'
    #     if to_token_name == 'USDC.e':
    #         to_token_name = 'USDC'
    #
    #     failed_text = f'Failed to swap {from_token_name} to {to_token_name} via Maverick'
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.MAVERICK)
    #
    #     from_token_price_dollar = await self.get_token_price(token_symbol=from_token_name)
    #     if to_token_name in ('BUSD', 'USDT'):
    #         to_token_price_dollar = 1
    #     else:
    #         to_token_price_dollar = await self.get_token_price(token_symbol=to_token_name)
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) * from_token_price_dollar / to_token_price_dollar * (100 - slippage) / 100,
    #         decimals=await self.client.transactions.get_decimals(contract=to_token_address)
    #     )
    #
    #     deadline = int(time.time() + 20 * 60)
    #     encoded_path = b''.join(path)
    #
    #     # exactInput params (path, recipient, deadline, amount, minAcquired)
    #     swap_amount_args = (
    #         encoded_path,
    #         f'{self.client.account.address}',
    #         deadline,
    #         amount.Wei,
    #         amount_out_min.Wei,
    #     )
    #     swap_amount_data = contract.encodeABI('exactInput', args=[swap_amount_args])
    #     # print(swap_amount_args)
    #     # print(swap_amount_data)
    #
    #     # refundETH params (None)
    #     return_eth_data = contract.encodeABI('refundETH', args=[])
    #
    #     # multicall params (data)
    #     swap_data = contract.encodeABI(
    #         'multicall',
    #         args=[
    #             [swap_amount_data, return_eth_data]
    #         ]
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=swap_data,
    #         value=amount.Wei
    #     )
    #
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via Maverick: {tx.hash.hex()}'
    #     return f'{failed_text}!'

    # async def _swap_token_to_eth(
    #         self,
    #         amount: TokenAmount,
    #         from_token: RawContract,
    #         slippage: float = 1
    # ) -> str:
    #     from_token_address = Web3.to_checksum_address(from_token.address)
    #     from_token = await self.client.contracts.default_token(contract_address=from_token_address)
    #     from_token_name = await from_token.functions.symbol().call()
    #
    #     path = self.PATH_MAP_SELL[from_token_name]
    #
    #     to_token_address = Web3.to_checksum_address(path[-1])
    #     to_token = await self.client.contracts.default_token(contract_address=to_token_address)
    #     to_token_name = await to_token.functions.symbol().call()
    #
    #     if from_token_name == 'WETH':
    #         from_token_name = 'ETH'
    #     if from_token_name == 'WBTC':
    #         from_token_name = 'BTC'
    #     if from_token_name == 'ceBUSD':
    #         from_token_name = 'BUSD'
    #     if from_token_name == 'USDC.e':
    #         from_token_name = 'USDC'
    #
    #     if to_token_name == 'WETH':
    #         to_token_name = 'ETH'
    #     if to_token_name == 'WBTC':
    #         to_token_name = 'BTC'
    #     if to_token_name == 'ceBUSD':
    #         to_token_name = 'BUSD'
    #     if to_token_name == 'USDC.e':
    #         to_token_name = 'USDC'
    #
    #     failed_text = f'Failed to swap {from_token_name} to {to_token_name} via Maverick'
    #
    #     if not amount:
    #         amount = await self.client.wallet.balance(token=from_token)
    #
    #     contract = await self.client.contracts.get(contract_address=Contracts.MAVERICK)
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
    #     to_token_price_dollar = await self.get_token_price(token_symbol=to_token_name)
    #
    #     amount_out_min = TokenAmount(
    #         amount=float(amount.Ether) / to_token_price_dollar * (1 - slippage / 100),
    #         decimals=await self.client.transactions.get_decimals(contract=to_token.address)
    #     )
    #
    #     deadline = int(time.time() + 20 * 60)
    #     encoded_path = b''.join(path)
    #
    #     # exactInput params (path, recipient, deadline, amount, minAcquired)
    #     swap_amount_args = (
    #         encoded_path,
    #         f'0x0000000000000000000000000000000000000000',
    #         deadline,
    #         amount.Wei,
    #         amount_out_min.Wei
    #     )
    #     swap_amount_data = contract.encodeABI('exactInput', args=[swap_amount_args])
    #
    #     # unwrapWETH9 params (None)
    #     return_token_data = contract.encodeABI('unwrapWETH9', args=[
    #         amount_out_min.Wei,
    #         f'{self.client.account.address}'
    #     ])
    #
    #     # multicall params (data)
    #     swap_data = contract.encodeABI(
    #         'multicall',
    #         args=[
    #             [swap_amount_data, return_token_data]
    #         ]
    #     )
    #
    #     tx_params = TxParams(
    #         to=contract.address,
    #         data=swap_data
    #     )
    #     # tx_params = await self.client.transactions.auto_add_params(tx_params)
    #     # return (await self.client.transactions.estimate_gas(tx_params)).Wei
    #
    #     tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
    #     receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
    #     if receipt:
    #         return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via Maverick: {tx.hash.hex()}'
    #     return f'{failed_text}!'

    async def _swap(
            self,
            path: list[bytes],
            amount: TokenAmount,
            slippage: float = 1.,
    ) -> str:
        from_token_address = Web3.to_checksum_address(path[0])
        from_token = await self.client.contracts.default_token(contract_address=from_token_address)
        from_token_name = await from_token.functions.symbol().call()

        to_token_address = Web3.to_checksum_address(path[-1])
        to_token = await self.client.contracts.default_token(contract_address=to_token_address)
        to_token_name = await to_token.functions.symbol().call()

        from_token_is_eth = from_token_address.upper() == Contracts.WETH.address.upper()

        if from_token_name == 'WETH':
            from_token_name = 'ETH'
        if from_token_name == 'WBTC':
            from_token_name = 'BTC'
        if from_token_name == 'ceBUSD':
            from_token_name = 'BUSD'
        if from_token_name == 'USDC.e':
            from_token_name = 'USDC'

        if to_token_name == 'WETH':
            to_token_name = 'ETH'
        if to_token_name == 'WBTC':
            to_token_name = 'BTC'
        if to_token_name == 'ceBUSD':
            to_token_name = 'BUSD'
        if to_token_name == 'USDC.e':
            to_token_name = 'USDC'

        failed_text = f'Failed to swap {from_token_name} to {to_token_name} via Maverick'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)

        contract = await self.client.contracts.get(contract_address=Contracts.MAVERICK)

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

        amount_of_min = TokenAmount(
            amount=float(amount.Ether) * (from_token_price_dollar / to_token_price_dollar) * (100 - slippage) / 100,
            decimals=await self.client.transactions.get_decimals(contract=to_token_address)
        )

        deadline = int(time.time() + 20 * 60)
        encoded_path = b''.join(path)

        if from_token_is_eth:
            swap_amount_args = (
                encoded_path,
                f'{self.client.account.address}',
                deadline,
                amount.Wei,
                amount_of_min.Wei
        )
        else:
            swap_amount_args = (
                encoded_path,
                f'0x0000000000000000000000000000000000000000',
                deadline,
                amount.Wei,
                amount_of_min.Wei
            )

        swap_amount_data = contract.encodeABI('exactInput', args=[swap_amount_args])

        print(swap_amount_args)
        print(swap_amount_data)

        if from_token_is_eth:
            second_item = contract.encodeABI('refundETH', args=[])
        else:
            second_item = contract.encodeABI('unwrapWETH9', args=[
                amount_of_min.Wei,
                f'{self.client.account.address}'
            ])

        swap_data = contract.encodeABI(
            'multicall',
            args=[
                [swap_amount_data, second_item]
            ]
        )

        tx_params = TxParams(
            to=contract.address,
            data=swap_data,
            value=amount.Wei if from_token_is_eth else 0
        )

        # tx_params = await self.client.transactions.auto_add_params(tx_params)
        # return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via Maverick: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_usdc(
            self,
            amount: TokenAmount,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_BUY['USDC.e'],
            slippage=slippage
        )

    async def swap_eth_to_busd(
            self,
            amount: TokenAmount,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_BUY['BUSD'],
            slippage=slippage
        )

    async def swap_usdc_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_SELL['USDC.e'],
            slippage=slippage
        )

    async def swap_busd_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_SELL['BUSD'],
            slippage=slippage
        )

    async def swap_eth_to_usdt(
            self,
            amount: TokenAmount,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_BUY['USDT'],
            slippage=slippage
        )

    async def swap_usdt_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage: float = 1.
    ) -> str:
        return await self._swap(
            amount=amount,
            path=Maverick.PATH_MAP_SELL['USDT'],
            slippage=slippage
        )
