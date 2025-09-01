import asyncio

from twitter.twitter import Twitter


async def main() -> None:
    twitter = Twitter()

    await twitter.guest_activate()
    print(twitter.guest_token)

    await twitter.flow_name_signup()
    print(twitter.flow_token)


if __name__ == "__main__":
    asyncio.run(main())
