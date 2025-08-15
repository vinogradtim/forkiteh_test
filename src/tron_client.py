from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from src.config import settings


class TronClient:

    def __init__(self):
        self.client = AsyncTron(network='mainnet', provider=AsyncHTTPProvider(api_key=settings.TRONGRID_API_KEY))

    async def get_wallet_info(self, address: str) -> dict:
        balance = await self.client.get_account_balance(address)
        bandwidth = await self.client.get_bandwidth(address)
        energy = await self.client.get_energy(address)
        return {"address": address, "balance": balance, "bandwidth": bandwidth, "energy": energy}
