import aiohttp


class Api(object):

    def __init__(self, method, uri) -> None:
        self._method = method
        self._uri = uri

    async def async_call_api(self, data, headers):
        async with aiohttp.ClientSession() as session:
            await session.request(
                self._method,
                self._uri,
                json=data,
                headers=headers
            )
