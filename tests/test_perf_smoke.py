import pytest

@pytest.mark.asyncio
async def test_openapi_loads(client):
    r = await client.get("/openapi.json")
    assert r.status_code == 200
    assert "paths" in r.json()
