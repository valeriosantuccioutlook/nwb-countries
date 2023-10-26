import pytest
from httpx import AsyncClient
from requests import Response
from starlette import status

from app.tests.v1.mocks import (
    COMPARABLE,
    FAKE,
    INVALID_COUNTRIES,
    ITALY,
    UK,
    VALID_COUNTRIES,
)

PREFIX: str = "/countries"
INFO_URL: str = PREFIX + "/{name}" + "/info"
CNAMES: str = "countries_names"
COMPARE: str = "compare"
COMPARE_URL: str = f"{PREFIX}/{COMPARE}"


@pytest.mark.anyio
async def test_retieve_country_info_italy(async_client: AsyncClient):
    response: Response = await async_client.get(INFO_URL.format(name=ITALY))
    response.json()
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_retieve_country_info_uk(async_client: AsyncClient):
    response: Response = await async_client.get(INFO_URL.format(name=UK))
    response.json()
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_retieve_country_info_fake(async_client: AsyncClient):
    response: Response = await async_client.get(INFO_URL.format(name=FAKE))
    response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.anyio
async def test_compare_valid_countries(async_client: AsyncClient):
    response: Response = await async_client.get(COMPARE_URL, params={CNAMES: VALID_COUNTRIES, COMPARE: COMPARABLE})
    response.json()
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_compare_invalid_countries(async_client: AsyncClient):
    response: Response = await async_client.get(COMPARE_URL, params={CNAMES: INVALID_COUNTRIES, COMPARE: COMPARABLE})
    response.json()
    assert response.status_code == status.HTTP_404_NOT_FOUND
