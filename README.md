# CRUD Application in Python

This project is a simple CRUD (Create, Read, Update, Delete) application implemented in Python. It provides a command-line interface (CLI) to manage items, stores data in a JSON file for persistence, includes error handling, and allows searching for items.

## Features

-   **Create:** Add new items to the system.
-   **Read:** Retrieve items by their unique ID.
-   **Update:** Modify existing items.
-   **Delete:** Remove items by their unique ID.
-   **Search:** Find items by name.
-   **Persistence:** Data is stored in a `data.json` file, ensuring data is preserved between sessions.
-   **Error Handling:** Handles cases where items are not found.
-   **Command-Line Interface:** User-friendly CLI for easy interaction.

## Getting Started

### Prerequisites

-   Python 3.x installed on your system.

### Running the Application

1.  **Clone the repository:**
```
bash
    git clone https://github.com/Dev-RuiDiniz/CRUD.git
    cd CRUD
    
```
2.  **Run the `main.py` file:**
```
bash
    python main.py
    
```
## Using the CLI

Once the application is running, you will be presented with a menu of options:
```
--- CRUD App Menu ---
1. Create item
2. Read item
3. Update item
4. Delete item
5. Search item
6. Exit
```
### Create Item

1.  Select `1` from the menu.
2.  Enter the name of the item when prompted.
3.  The application will confirm that the item was created and display its ID.

### Read Item

1.  Select `2` from the menu.
2.  Enter the ID of the item you want to read.
3.  If the item exists, its details will be displayed. Otherwise, an error message will be shown.

### Update Item

1.  Select `3` from the menu.
2.  Enter the ID of the item you want to update.
3.  Enter the new name for the item.
4.  The application will confirm that the item has been updated.

### Delete Item

1.  Select `4` from the menu.
2.  Enter the ID of the item you want to delete.
3.  The application will confirm that the item has been deleted.

### Search Item

1.  Select `5` from the menu.
2.  Enter the name (or part of the name) of the item you want to search for.
3.  The application will display a list of items that match the search query.

### Exit

1.  Select `6` from the menu to exit the application.

## Data Persistence

All data is stored in the `data.json` file. This file is created automatically in the project's root directory when you create your first item.

## Error Handling

The application handles cases where you try to read or delete a non-existent item. In such cases, an appropriate error message will be displayed.