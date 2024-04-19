from bybit.models import ByBitCredentials
from py_okx_async.models import OKXCredentials


bybit_api_key = 'zAOYBAf7jFZWgcbgxw'
bybit_secret_key = 'VD5M2W51QSQ5AptKRlQ7jvYcAiA4hShh7CEx'

okx_api_key = '41356af3-0a72-4a7c-90b8-0a0e168a0898'
okx_secret_key = '32AB2AAB400B8D717DE3BE80CCA10BC9'
okx_passphrase = '&12324p4~425KT+5?iaAGndfj33333'

bybit_credentials = ByBitCredentials(api_key=bybit_api_key, api_secret=bybit_secret_key)

okx_credentials = OKXCredentials(
    api_key=okx_api_key,
    secret_key=okx_secret_key,
    passphrase=okx_passphrase
)
