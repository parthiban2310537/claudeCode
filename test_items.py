import items as items_module


def setup_function():
    items_module.items_store.clear()


def test_list_all_empty():
    assert items_module.list_all_items() == []


def test_list_all_returns_all_items():
    items_module.add_item("Apple", "A red fruit")
    items_module.add_item("Banana", "A yellow fruit")
    result = items_module.list_all_items()
    assert len(result) == 2
    assert result[0]["name"] == "Apple"
    assert result[1]["name"] == "Banana"


def test_list_all_returns_copy():
    items_module.add_item("Apple")
    result = items_module.list_all_items()
    result.clear()
    assert len(items_module.list_all_items()) == 1


def test_add_item_assigns_id():
    item = items_module.add_item("Cherry", "A small red fruit")
    assert item["id"] == 1
    assert item["name"] == "Cherry"


def test_get_item():
    items_module.add_item("Apple")
    item = items_module.get_item(1)
    assert item is not None
    assert item["name"] == "Apple"


def test_get_item_not_found():
    assert items_module.get_item(99) is None


def test_delete_item():
    items_module.add_item("Apple")
    assert items_module.delete_item(1) is True
    assert items_module.list_all_items() == []


def test_delete_item_not_found():
    assert items_module.delete_item(99) is False
