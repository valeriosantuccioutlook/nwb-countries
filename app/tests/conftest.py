import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import nwb

client: TestClient = TestClient(nwb)


@pytest.fixture()
async def async_client():
    async with AsyncClient(app=nwb, base_url=f"{client.base_url}/v{nwb.version}") as async_client:
        yield async_client


@pytest.fixture
def anyio_backend():
    return "asyncio"
