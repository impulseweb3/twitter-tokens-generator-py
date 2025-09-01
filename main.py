import asyncio

from twitter import Twitter


async def main() -> None:
    twitter = Twitter()

    await twitter.guest_activate()
    print(twitter.guest_token)


if __name__ == "__main__":
    asyncio.run(main())
