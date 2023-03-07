from httpx import AsyncClient


class PokeApiTransport:

    @staticmethod
    async def get_content(url: str):

        async with AsyncClient() as client:
            response = await client.get(url=url)

        if response.status_code != 200:
            raise Exception()

        return response.content

    @staticmethod
    async def get_poke_api_url(url_option, url_value):
        base_url = "https://pokeapi.co/api/v2"

        poke_urls = {
            "species": "{}/pokemon-species/{}/".format(base_url, url_value),
            "id": "{}/pokemon/{}/".format(base_url, url_value),
            "name": "{}/pokemon/{}/".format(base_url, url_value),

        }

        url = poke_urls.get(url_option)

        return url
