import pytest
from repository.db import DB
from domain.types import AgedBrie


@pytest.mark.db
def test_get_item():
    item = ["Aged Brie", 2, 0]
    assert item == DB.get_item("Aged Brie")

@pytest.mark.db
def test_get_objeto():
    item = AgedBrie("Aged Brie", 2, 0)
    assert item == DB.get_objeto("Aged Brie")
