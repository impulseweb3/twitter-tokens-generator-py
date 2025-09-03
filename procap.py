import os

from httpx import AsyncClient


class Procap:
    asyncClient: AsyncClient

    def __init__(self) -> None:
        self.asyncClient = AsyncClient()

    async def get_balance(self) -> float:
        json = {
            "key": os.getenv("PROCAP"),
        }

        response = await self.asyncClient.post(
            "https://api.procap.wtf/users/getUser",
            json=json
        )

        return response.json()["balance"]

    async def get_token(self, proxy: str) -> str:
        json = {
            "public_key": "2CB16598-CB82-4CF7-B332-5990DB66F3AB",
            "proxy": proxy,
            "key": os.getenv("PROCAP"),
            "captchaType": "funcaptcha",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"130\", \"Chromium\";v=\"130\", \"Not_A Brand\";v=\"24\"",
        }

        response = await self.asyncClient.post(
            "https://api.procap.wtf/solve",
            json=json,
            timeout=60,
        )

        return response.json()["token"]
