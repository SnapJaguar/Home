import pytest
from httpx import AsyncClient, ASGITransport
from main2 import app


@pytest.mark.anyio
async def test_read_root():
    # Для новых версий httpx передаем приложение через ASGITransport
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Привет! Это твой REST сервис."}
