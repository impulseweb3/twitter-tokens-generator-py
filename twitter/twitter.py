from twikit import Client

from twitter.begin_verification import BeginVerification
from twitter.flow_name_signup import FlowNameSignup
from twitter.guest_activate import GuestActivate


class Twitter:
    client: Client
    guest_token: str
    flow_token: str

    def __init__(self) -> None:
        self.client = Client()
        self.guest_token = str()
        self.flow_token = str()

    async def guest_activate(self) -> None:
        await GuestActivate(self).guest_activate()

    async def flow_name_signup(self) -> None:
        await FlowNameSignup(self).flow_name_signup()

    async def begin_verification(self, email: str, display_name: str) -> None:
        await BeginVerification(self).begin_verification(email, display_name)
