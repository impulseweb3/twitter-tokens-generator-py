import asyncio

import dotenv

from emailnator import Emailnator
from procap import Procap
from twitter.twitter import Twitter


async def main() -> None:
    dotenv.load_dotenv()

    proxy = 'http://qxwltgrb:gxoxa8007tc7@23.95.150.145:6114'

    twitter = Twitter(proxy)

    emailnator = Emailnator(proxy)
    await emailnator.fetch_cookies()

    procap = Procap()

    await twitter.guest_activate()
    print(twitter.guest_token)

    await twitter.flow_name_signup()
    print(twitter.flow_token)

    email = str()
    valid = False
    while not valid:
        email = await emailnator.get_email()
        valid = await twitter.email_available(email)
    print(email)

    await twitter.begin_verification(email, 'John Doe')
    print('begin_verification')

    code = None
    while not code:
        code = await emailnator.get_code(email)
    print(code)

    access_token = await procap.get_token(proxy)
    print(access_token)

    await twitter.email_verification('John Doe', email, access_token, code)
    print(twitter.flow_token)


if __name__ == '__main__':
    asyncio.run(main())
