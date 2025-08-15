from httpx import AsyncClient, ASGITransport

import pytest

from src.db.repositories import WalletQueryRepository
from src.tron_client import TronClient
from src.main import app


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


class FakeTronClient:
    async def get_wallet_info(self, address: str) -> dict:
        return {"address": address, "balance": 123.12, "bandwidth": 123, "energy": 31}


class FakeWalletQueryRepository:
    async def save_wallet_query(self, address: str, balance: float, bandwidth: int, energy: int) -> dict:
        return {'status': 'saved'}


app.dependency_overrides[TronClient] = lambda: FakeTronClient()
app.dependency_overrides[WalletQueryRepository] = lambda: FakeWalletQueryRepository()


@pytest.fixture
def tron_client():
    return FakeTronClient()
