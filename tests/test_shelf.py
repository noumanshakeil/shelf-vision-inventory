import pytest

@pytest.mark.asyncio
async def test_shelf_restock(client):
    s = await client.post("/api/scans", json={"aisle": "B2", "raw_text": "SKU-100 SKU-200"})
    sid = s.json()["id"]
    await client.post(f"/api/scans/{sid}/gaps", json={"expected": {"SKU-100": 5}})
    r = await client.post(f"/api/scans/{sid}/restock")
    assert r.status_code == 200
