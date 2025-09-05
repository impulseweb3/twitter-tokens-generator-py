from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from twitter.twitter import Twitter


class EmailAvailable:
    twitter: 'Twitter'

    def __init__(self, twitter: 'Twitter') -> None:
        self.twitter = twitter

    async def email_available(self, email: str) -> bool:
        cookies = {
            'gt': self.twitter.guest_token,
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
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
            'x-guest-token': self.twitter.guest_token,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en-US',
        }

        params = {
            'email': email,
        }

        json, _ = await self.twitter.client.get(
            'https://api.x.com/i/users/email_available.json',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        return json['valid']
