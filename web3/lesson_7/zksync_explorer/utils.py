import aiohttp
from curl_cffi.requests import AsyncSession

import exceptions


def aiohttp_params(params: dict[str, ...] | None) -> dict[str, str | int | float] | None:
    """
    Convert requests params to aiohttp params.

    Args:
        params (Optional[Dict[str, Any]]): requests params.

    Returns:
        Optional[Dict[str, Union[str, int, float]]]: aiohttp params.

    """
    new_params = params.copy()
    if not params:
        return

    for key, value in params.items():
        if value is None:
            del new_params[key]

        if isinstance(value, bool):
            new_params[key] = value.decode('utf-8')

    return new_params


async def async_get(url: str, headers: dict | None = None, **kwargs) -> dict | None:
    """
    Make a GET request and check if it was successful.

    Args:
        url (str): a URL.
        headers (Optional[dict]): the headers. (None)
        **kwargs: arguments for a GET request, e.g. 'params', 'headers', 'data' or 'json'.

    Returns:
        Optional[dict]: received dictionary in response.

    """
    async with AsyncSession() as session:
        response = await session.get(
            url=url,
            headers=headers,
            **kwargs,
            # params=params,
            # proxy=proxy_url
        )
        status_code = response.status_code
        response = response.json()
        if status_code <= 201:
            return response
        raise exceptions.HTTPException(response=response, status_code=status_code)


def api_key_required(func):
    """Check if the Blockscan API key is specified."""

    def func_wrapper(self, *args, **kwargs):
        if not self.client.network.api.key or not self.client.network.api.functions:
            raise exceptions.APIException('To use this function, you must specify the explorer API key!')

        else:
            return func(self, *args, **kwargs)

    return func_wrapper