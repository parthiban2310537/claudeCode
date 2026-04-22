items_store = []


def add_item(name: str, description: str = "") -> dict:
    item = {"id": len(items_store) + 1, "name": name, "description": description}
    items_store.append(item)
    return item


def list_all_items() -> list:
    return list(items_store)


def get_item(item_id: int) -> dict | None:
    return next((i for i in items_store if i["id"] == item_id), None)


def delete_item(item_id: int) -> bool:
    for idx, item in enumerate(items_store):
        if item["id"] == item_id:
            items_store.pop(idx)
            return True
    return False


if __name__ == "__main__":
    add_item("Apple", "A red fruit")
    add_item("Banana", "A yellow fruit")
    add_item("Cherry", "A small red fruit")

    print("All items:")
    for item in list_all_items():
        print(f"  [{item['id']}] {item['name']} - {item['description']}")
