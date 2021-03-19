import pytest


@pytest.mark.item
def test_item(client):    
    rv = client.get('/item/Aged Brie')
    # assert b'["Aged Brie", 2, 0]' in rv.data
    assert {"name": "Aged Brie", "sell_in": 2, "quality": 0} == rv.get_json()
