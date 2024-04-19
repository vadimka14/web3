from datetime import datetime, timedelta

from fake_useragent import UserAgent

# from zksync_explorer.utils import async_get, aiohttp_params
from utils import async_get, aiohttp_params


async def get_txs_explorer(
        account_address: str,
        page_size: int = 10,
        page: int = 1,
) -> dict[str, ...]:
    headers = {
        'authority': 'block-explorer-api.mainnet.zksync.io',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://explorer.zksync.io',
        'referer': 'https://explorer.zksync.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': UserAgent().random,
    }

    now = datetime.now() - timedelta(hours=3)
    formatted_date = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    params = {
        'address': account_address,
        'pageSize': str(page_size),
        'page': str(page),
        # 'toDate': '2024-02-20T12:04:24.511Z',
        'toDate': formatted_date,
    }

    return await async_get(
        url='https://block-explorer-api.mainnet.zksync.io/transactions',
        params=aiohttp_params(params),
        headers=headers
    )


class Module:
    """
        Class with functions related to some API module.

        Attributes:
            key (str): an API key.
            url (str): an API entrypoint URL.
            headers (Dict[str, Any]): a headers for requests.
            module (str): a module name.

        """
    key: str
    url: str
    headers: dict[str, ...]
    module: str

    def __init__(self, key: str, url: str, headers: dict[str, ...]) -> None:
        """
        Initialize the class.

        Args:
            key (str): an API key.
            url (str): an API entrypoint URL.
            headers (Dict[str, Any]): a headers for requests.

        """
        self.key = key
        self.url = url
        self.headers = headers


class Account(Module):
    module: str = 'address'

    async def txlist(
            self,
            address: str,
            page: int = 1,
            limit: int = 50,
            chain: str | None = 'zksync'
    ) -> list[dict]:
        """
        Query address transaction list information

        https://www.oklink.com/docs/en/#blockchain-general-api-address-query-address-transaction-list-information
        """

        action = 'transaction-list'

        params = {
            'chainShortName': chain,
            'address': address,
            'limit': limit,
            'page': page
        }

        res = await async_get(
            url=self.url + f'/api/v5/explorer/{self.module}/{action}',
            params =aiohttp_params(params),
            headers=self.headers
        )

        # print(res)
        # total_page = res['data'][0]['totalPage']
        return res['data'][0]['transactionLists']

    async def txlist_all(
            self,
            address: str,
            chain: str | None = 'zksync',
    ) -> list[dict]:
        page = 1
        limit = 50
        txs_lst = []
        txs = await self.txlist(
            address=address,
            page=page,
            limit=limit,
            chain=chain,
        )
        txs_lst += txs
        while len(txs) == limit:
            page += 1
            txs = await self.txlist(
                address=address,
                page=page,
                limit=limit,
                chain=chain,
            )
            txs_lst += txs
        return txs_lst

    async def find_tx_by_method_id(
            self,
            address: str,
            to: str, method_id: str,
    ):
        txs = {}
        coin_txs = await self.txlist_all(address=address)
        for tx in coin_txs:
            # {'txId': '0x12364b581306d4d24dfa7a932b824d5138dd2aa438d37df89c3f2b53e28ec3ca', 'methodId': '0x6c0960f9', 'blockHash': '0xda45c43705df9e618c6cb7da3b140337f66ee29658c8e718a14d0e930c37ec19', 'height': '27164388', 'transactionTime': '1708546781000', 'from': '0x7277a1e840b1eef3e649b83483366d35f4e98fae', 'to': '0x32400084c286cf3e17e7b677ea9583e60a000324', 'isFromContract': False, 'isToContract': False, 'amount': '0', 'transactionSymbol': 'ETH', 'txFee': '0.0000289515', 'state': 'success', 'tokenId': '', 'tokenContractAddress': '', 'challengeStatus': '', 'l1OriginHash': ''}
            if tx.get('state') == 'success' and tx.get('to') == to.lower() and method_id in tx.get('methodId'):
                txs[tx.get('txId')] = tx
        return txs


class APIFunctions:
    """
    Class with functions related to Blockscan API.

    Attributes:
        key (str): an API key.
        url (str): an API entrypoint URL.
        headers (Dict[str, Any]): a headers for requests.
        account (Account): functions related to 'account' API module.

    """

    def __init__(self, key: str, url: str) -> None:
        """
        Initialize the class.

        Args:
            key (str): an API key.
            url (str): an API entrypoint URL.

        """
        self.key = key
        self.url = url
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'user-agent': UserAgent().chrome,
            'Ok-Access-Key': self.key,
        }
        self.account = Account(self.key, self.url, self.headers)


