from twikit import Client


class Twitter:
    client: Client
    guest_token: str

    def __init__(self) -> None:
        self.client = Client()
        self.guest_token = str()

    async def guest_activate(self) -> None:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            # 'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://x.com',
            'priority': 'u=1, i',
            'referer': 'https://x.com/',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en-US',
        }

        json, _ = await self.client.post(
            'https://api.x.com/1.1/guest/activate.json',
            headers=headers,
        )

        self.guest_token = json["guest_token"]
