import time
import asyncio
import random

from web3 import Web3
from web3.types import TxParams

from tasks.base import Base
from eth_async.models import RawContract, TxArgs, TokenAmount, DefaultABIs, Network, Networks
from data.models import Contracts


'''0xd7570e45
0000000000000000000000000000000000000000000000000000000000000060
000000000000000000000000000000000000000000000000000000000004fe9f - amountIn
00000000000000000000000000000000000000000000000000000000660d4040 - deadline
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000020
0000000000000000000000000000000000000000000000000000000000000060
0000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000005af3107a4000 - amountOut
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000020
00000000000000000000000080115c708e12edd42e504c1cd52aea96c547c05c - pool
00000000000000000000000000000000000000000000000000000000000000a0
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000120
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000060
0000000000000000000000005aea5775959fbc2557cc8789bc1bf90a239d9a91 - WETH
0000000000000000000000007131b37478af63e775402248583099974a005b75 - address
0000000000000000000000000000000000000000000000000000000000000002
0000000000000000000000000000000000000000000000000000000000000000







0xd7570e45
000 0000000000000000000000000000000000000000000000000000000000000060  + link
020 000000000000000000000000000000000000000000000000000002b9fd81a093 - amountOUt +
040 00000000000000000000000000000000000000000000000000000000660d6ca8 - deadline +
060 0000000000000000000000000000000000000000000000000000000000000001 +
080 0000000000000000000000000000000000000000000000000000000000000020 +
0a0 0000000000000000000000000000000000000000000000000000000000000060 +
0c0 0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC + 
0e0 0000000000000000000000000000000000000000000000000000000000002710 - amountIn +
100 0000000000000000000000000000000000000000000000000000000000000001 +
120 0000000000000000000000000000000000000000000000000000000000000020 +
140 00000000000000000000000080115c708e12edd42e504c1cd52aea96c547c05c - pool +
160 00000000000000000000000000000000000000000000000000000000000000a0
180 0000000000000000000000000000000000000000000000000000000000000000
1a0 0000000000000000000000000000000000000000000000000000000000000120
    0000000000000000000000000000000000000000000000000000000000000001
    0000000000000000000000000000000000000000000000000000000000000060
    0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC +
    0000000000000000000000007131b37478af63e775402248583099974a005b75 - address +
    0000000000000000000000000000000000000000000000000000000000000001 +
    0000000000000000000000000000000000000000000000000000000000000000 +


0x2cc4081e
0000000000000000000000000000000000000000000000000000000000000060 +
0000000000000000000000000000000000000000000000000000880ea8c8e490 amountOUt +
00000000000000000000000000000000000000000000000000000000660d56d4 deadline +
0000000000000000000000000000000000000000000000000000000000000001 +
0000000000000000000000000000000000000000000000000000000000000020 +
0000000000000000000000000000000000000000000000000000000000000060 +
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC +
00000000000000000000000000000000000000000000000006f05b59d3b20000 - amountIn +
0000000000000000000000000000000000000000000000000000000000000001 +
0000000000000000000000000000000000000000000000000000000000000020 +
00000000000000000000000080115c708e12edd42e504c1cd52aea96c547c05c - pool +
0000000000000000000000000000000000000000000000000000000000000080
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000100
тут строка з 01
0000000000000000000000000000000000000000000000000000000000000060
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4 - USDC +
0000000000000000000000007131b37478af63e775402248583099974a005b75 - address +
0000000000000000000000000000000000000000000000000000000000000001 +
0000000000000000000000000000000000000000000000000000000000000000 +
'''
'''0x2cc4081e
0000000000000000000000000000000000000000000000000000000000000060
000000000000000000000000000000000000000000000000000088193058b4d6
00000000000000000000000000000000000000000000000000000000660d5b1c
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000020
0000000000000000000000000000000000000000000000000000000000000060
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4
00000000000000000000000000000000000000000000000006f05b59d3b20000
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000020
00000000000000000000000080115c708e12edd42e504c1cd52aea96c547c05c
0000000000000000000000000000000000000000000000000000000000000080
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000120
0000000000000000000000000000000000000000000000000000000000000080
0000000000000000000000003355df6d4c9c3035724fd0e3914de96a5a83aaf4
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000007131b37478af63e775402248583099974a005b75
0000000000000000000000000000000000000000000000000000000000000001
0000000000000000000000000000000000000000000000000000000000000000'''


class SyncSwap(Base):
    async def swap_eth_to_usdc(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        to_token = Contracts.USDC

        to_token = await self.client.contracts.default_token(contract_address=to_token.address)
        to_token_name = await to_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {to_token_name} via SyncSwap'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        eth_price = await self.get_token_price(token_symbol='ETH')
        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
            decimals=await self.client.transactions.get_decimals(contract=to_token)
        )

        pool = Web3.to_checksum_address('0x80115c708e12edd42e504c1cd52aea96c547c05c')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.WETH.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
            value=amount.Wei
        )

        self.parse_params(tx_params['data'])

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} ETH was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_usdc_to_eth(
            self,
            amount: TokenAmount | None = None,
            slippage: float = 1.
    ) -> str:
        from_token = await self.client.contracts.default_token(contract_address=Contracts.USDC.address)
        from_token_name = await from_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {from_token_name} via SyncSwap'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)
            if not amount.Wei:
                return f'{failed_text}: {self.client.account.address} | SyncSwap | swap_token | ' \
                       f'not enough {from_token_name} balance ({amount.Ether})'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        if await self.approve_interface(
                token_address=from_token.address,
                spender=contract.address,
                amount=amount
        ):
            await asyncio.sleep(random.randint(5, 10))
        else:
            return f'{failed_text} | can not approve'

        eth_price = await self.get_token_price(token_symbol='ETH')

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
        )

        pool = Web3.to_checksum_address('0x80115c708e12edd42e504c1cd52aea96c547c05c')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.USDC.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"1".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()
                    ],
                    tokenIn=Contracts.USDC.address,
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
        )

        self.parse_params(tx_params['data'])
        return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_usdt(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        to_token = Contracts.USDT

        to_token = await self.client.contracts.default_token(contract_address=to_token.address)
        to_token_name = await to_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {to_token_name} via SyncSwap'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        eth_price = await self.get_token_price(token_symbol='ETH')
        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
            decimals=await self.client.transactions.get_decimals(contract=to_token)
        )

        pool = Web3.to_checksum_address('0xd3d91634cf4c04ad1b76ce2c06f7385a897f54d3')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.WETH.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
            value=amount.Wei
        )

        # self.parse_params(tx_params['data'])
        # return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} ETH was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_busd(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        to_token = Contracts.ceBUSD

        to_token = await self.client.contracts.default_token(contract_address=to_token.address)
        to_token_name = await to_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {to_token_name} via SyncSwap'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        eth_price = await self.get_token_price(token_symbol='ETH')
        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * eth_price * (1 - slippage / 100),
            decimals=await self.client.transactions.get_decimals(contract=to_token)
        )

        pool = Web3.to_checksum_address('0xad86486f1d225d624443e5df4b2301d03bbe70f6')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.WETH.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
            value=amount.Wei
        )

        # self.parse_params(tx_params['data'])
        # return

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} ETH was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_wbtc(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        to_token = Contracts.WBTC

        to_token = await self.client.contracts.default_token(contract_address=to_token.address)
        to_token_name = await to_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {to_token_name} via SyncSwap'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        eth_price = await self.get_token_price(token_symbol='ETH')
        wbtc_price = await self.get_token_price(token_symbol='BTC')
        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * eth_price / wbtc_price * (1 - slippage / 100),
            decimals=await self.client.transactions.get_decimals(contract=to_token)
        )

        pool = Web3.to_checksum_address('0xb3479139e07568ba954c8a14d5a8b3466e35533d')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.WETH.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
            value=amount.Wei
        )

        # self.parse_params(tx_params['data'])
        # return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} ETH was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_usdt_to_eth(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        from_token = await self.client.contracts.default_token(contract_address=Contracts.USDT.address)
        from_token_name = await from_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {from_token_name} via SyncSwap'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)
            if not amount.Wei:
                return f'{failed_text}: {self.client.account.address} | SyncSwap | swap_token | ' \
                       f'not enough {from_token_name} balance ({amount.Ether})'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        if await self.approve_interface(
                token_address=from_token.address,
                spender=contract.address,
                amount=amount
        ):
            await asyncio.sleep(random.randint(5, 10))
        else:
            return f'{failed_text} | can not approve'

        eth_price = await self.get_token_price(token_symbol='ETH')

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
        )

        pool = Web3.to_checksum_address('')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.USDT.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn=Contracts.USDT.address,
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
        )

        # self.parse_params(tx_params['data'])
        # return

        # tx_params = await self.client.transactions.auto_add_params(tx_params)
        # return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_busd_to_eth(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        from_token = await self.client.contracts.default_token(contract_address=Contracts.ceBUSD.address)
        from_token_name = await from_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {from_token_name} via SyncSwap'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)
            if not amount.Wei:
                return f'{failed_text}: {self.client.account.address} | SyncSwap | swap_token | ' \
                       f'not enough {from_token_name} balance ({amount.Ether})'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        if await self.approve_interface(
                token_address=from_token.address,
                spender=contract.address,
                amount=amount
        ):
            await asyncio.sleep(random.randint(5, 10))
        else:
            return f'{failed_text} | can not approve'

        eth_price = await self.get_token_price(token_symbol='ETH')

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) / eth_price * (1 - slippage / 100),
        )

        pool = Web3.to_checksum_address('0xad86486f1d225d624443e5df4b2301d03bbe70f6')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.ceBUSD.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn=Contracts.ceBUSD.address,
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
        )

        # self.parse_params(tx_params['data'])
        # return

        # tx_params = await self.client.transactions.auto_add_params(tx_params)
        # return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_wbtc_to_eth(
            self,
            amount: TokenAmount,
            slippage: float = 1.0
    ) -> str:
        from_token = await self.client.contracts.default_token(contract_address=Contracts.WBTC.address)
        from_token_name = await from_token.functions.symbol().call()

        failed_text = f'Failed swap ETH to {from_token_name} via SyncSwap'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)
            if not amount.Wei:
                return f'{failed_text}: {self.client.account.address} | SyncSwap | swap_token | ' \
                       f'not enough {from_token_name} balance ({amount.Ether})'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        if await self.approve_interface(
                token_address=from_token.address,
                spender=contract.address,
                amount=amount
        ):
            await asyncio.sleep(random.randint(5, 10))
        else:
            return f'{failed_text} | can not approve'

        eth_price = await self.get_token_price(token_symbol='ETH')
        wbtc_price = await self.get_token_price(token_symbol='BTC')

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * wbtc_price/ eth_price * (1 - slippage / 100),
        )

        pool = Web3.to_checksum_address('0xb3479139e07568ba954c8a14d5a8b3466e35533d')

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool,
                            data=f'0x{Contracts.WBTC.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{"2".zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn=Contracts.WBTC.address,
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
        )

        # self.parse_params(tx_params['data'])
        # return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

