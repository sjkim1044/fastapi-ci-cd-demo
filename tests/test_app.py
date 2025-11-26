from app.main import health_check, list_items, add_item

def test_health():
    assert health_check() == {"status": "ok"}

def test_add_item():
    add_item("apple")
    add_item("banana")
    assert list_items() == {"items": ["apple", "banana"]}
