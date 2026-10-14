from backend.repositories import audit

def test_audit_ring_buffer():
    audit.record("unit", "ok")
    assert audit.recent(1)[0]["event"] == "unit"
