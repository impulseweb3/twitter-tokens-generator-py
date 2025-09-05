from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from twitter.twitter import Twitter


class EmailVerification:
    twitter: 'Twitter'

    def __init__(self, twitter: 'Twitter') -> None:
        self.twitter = twitter

    async def email_verification(self, name: str, email: str, access_token: str, code: str) -> None:
        cookies = {
            'gt': self.twitter.guest_token,
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
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

        json_data = {
            'flow_token': self.twitter.flow_token,
            'subtask_inputs': [
                {
                    'subtask_id': 'Signup',
                    'sign_up': {
                        'link': 'email_next_link',
                        'name': name,
                        'email': email,
                        'birthday': {
                            'day': 1,
                            'month': 1,
                            'year': 2000,
                        },
                        'personalization_settings': {
                            'allow_cookie_use': False,
                            'allow_device_personalization': False,
                            'allow_partnerships': False,
                            'allow_ads_personalization': False,
                        },
                    },
                },
                {
                    'subtask_id': 'SignupSettingsListEmail',
                    'settings_list': {
                        'setting_responses': [
                            {
                                'key': 'allow_emails_about_activity',
                                'response_data': {
                                    'boolean_data': {
                                        'result': False,
                                    },
                                },
                            },
                            {
                                'key': 'find_by_email',
                                'response_data': {
                                    'boolean_data': {
                                        'result': False,
                                    },
                                },
                            },
                            {
                                'key': 'personalize_ads',
                                'response_data': {
                                    'boolean_data': {
                                        'result': False,
                                    },
                                },
                            },
                        ],
                        'link': 'next_link',
                    },
                },
                {
                    'subtask_id': 'ArkoseEmail',
                    'web_modal': {
                        'completion_deeplink': f'twitter://onboarding/web_modal/next_link?access_token={access_token}',
                        'link': 'signup_with_email_next_link',
                    },
                },
                {
                    'subtask_id': 'EmailVerification',
                    'email_verification': {
                        'code': code,
                        'email': email,
                        'link': 'next_link',
                    },
                },
            ],
        }

        json, _ = await self.twitter.client.post(
            'https://api.x.com/1.1/onboarding/task.json',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        self.twitter.flow_token = json['flow_token']
