
# Grocery List Manager 

A Python-based console application for efficient grocery shopping management with categorized items and data persistence.

## Features

- ** List Management** - Create, edit, and manage multiple grocery lists
- ** Categorized Items** - Organize groceries by categories (Produce, Dairy, etc.)
- ** Data Persistence** - Automatic saving and loading of all data
- ** Purchase Tracking** - Mark items as purchased/unpurchased
- ** Progress Monitoring** - Track shopping completion status

## Project Structure
.
├── main.py # Main application entry point
├── ListManager.py # Core list management logic
├── GroceryItem.py # Item class definition
├── categories.py # Category management system
├── DataStore/ # Data persistence layer
├── pycache/ # Python compiled files
└── README.md

text

## Modules Description

###  Core Modules
- **`main.py`** - Application entry point and user interface
- **`ListManager.py`** - Handles list operations (create, read, update, delete)
- **`GroceryItem.py`** - Defines item properties and behaviors

###  Support Modules
- **`categories.py`** - Manages item categorization system
- **`DataStore/`** - Handles data persistence and file operations

## Installation & Usage

1. **Ensure Python 3.x is installed** on your system

2. **Run the application:**
   ```bash
   python main.py
Follow the menu prompts to:

Create new grocery lists

Add items with categories

Mark items as purchased

View list progress

Data Storage
All your grocery lists and items are automatically saved in the DataStore/ directory and persist between sessions.

Technical Details
Language: Python 3.x

Architecture: Modular with separation of concerns

Storage: File-based persistence

Pattern: Object-Oriented Programming

Example Usage
text
=== GROCERY LIST MANAGER ===
1. Create New List
2. View Existing Lists
3. Add Item to List
4. Mark Item Purchased
5. View List Progress
6. Exit
