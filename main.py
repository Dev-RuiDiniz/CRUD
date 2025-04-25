import json
import os

DATA_FILE = "data.json"

def load_data():
    """Loads data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return data, data[-1]["id"] + 1 if data else 1
            except json.JSONDecodeError:
                return [], 1
    else:
        return [], 1

def save_data(data):
    """Saves data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data, next_id = load_data()


def create(item):
    """Creates a new item and adds it to the data."""
    global next_id
    item["id"] = next_id
    data.append(item)
    next_id += 1
    save_data(data)
    print(f"Item '{item['name']}' created with ID {item['id']}.")


def read(item_id):
    """Reads an item from the data by its ID."""
    for item in data:
        if item["id"] == item_id:
            return item
    raise ValueError(f"Item with ID {item_id} not found.")


def update(item_id, updated_item):
    """Updates an existing item."""
    try:
        item = read(item_id)
        item.update(updated_item)
        save_data(data)
        print(f"Item with ID {item_id} updated.")
    except ValueError as e:
        print(e)


def delete(item_id):
    """Deletes an item from the data by its ID."""    
    try:
        global data
        item = read(item_id)
        data.remove(item)
        save_data(data)
        print(f"Item with ID {item_id} deleted.")
    except ValueError as e:
        print(e)

def search(item_name):
    """Search for items by name."""
    results = [item for item in data if item_name.lower() in item["name"].lower()]
    return results


def display_menu():
    """Displays the command-line menu."""
    print("\n--- CRUD App Menu ---")
    print("1. Create item")
    print("2. Read item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search item")
    print("6. Exit")


def main():
    """Main function to run the command-line interface."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            create({"name": name})
        elif choice == "2":
            try:
                item_id = int(input("Enter item ID to read: "))
                item = read(item_id)
                print("Item found:", item)
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                item_id = int(input("Enter item ID to update: "))
                new_name = input("Enter new item name: ")
                update(item_id, {"name": new_name})
            except ValueError as e:
                print(e)
        elif choice == "4":
            item_id = int(input("Enter item ID to delete: "))
            delete(item_id)
        elif choice == "5":
            item_name = input("Enter item name to search: ")
            results = search(item_name)
            print("Search results:", results)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
