from urllib import parse

from httpx import AsyncClient


class Emailnator:
    asyncClient: AsyncClient
    xsrf_token: str
    gmailnator_session: str

    def __init__(self, proxy: str) -> None:
        self.asyncClient = AsyncClient(proxy=proxy)
        self.xsrf_token = str()
        self.gmailnator_session = str()

    async def fetch_cookies(self) -> None:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'fr',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        }

        response = await self.asyncClient.get(
            'https://www.emailnator.com/',
            headers=headers,
        )

        self.xsrf_token = response.cookies['XSRF-TOKEN']
        self.gmailnator_session = response.cookies['gmailnator_session']

    async def get_email(self) -> str:
        cookies = {
            'XSRF-TOKEN': self.xsrf_token,
            'gmailnator_session': self.gmailnator_session,
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'fr',
            'content-type': 'application/json',
            'origin': 'https://www.emailnator.com',
            'priority': 'u=1, i',
            'referer': 'https://www.emailnator.com/',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': parse.unquote(self.xsrf_token),
        }

        json_data = {
            'email': [
                'dotGmail',
            ],
        }

        response = await self.asyncClient.post(
            'https://www.emailnator.com/generate-email',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        return response.json()['email'][0]

    async def get_code(self, email: str) -> str | None:
        cookies = {
            'XSRF-TOKEN': self.xsrf_token,
            'gmailnator_session': self.gmailnator_session,
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'fr',
            'content-type': 'application/json',
            'origin': 'https://www.emailnator.com',
            'priority': 'u=1, i',
            'referer': 'https://www.emailnator.com/mailbox/',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': parse.unquote(self.xsrf_token),
        }

        json_data = {
            'email': email,
        }

        response = await self.asyncClient.post(
            'https://www.emailnator.com/message-list',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=60,
        )

        for message in response.json()['messageData']:
            if message['from'] == 'X <info@x.com>':
                return message['subject'][:6]

        return None
