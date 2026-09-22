"""
Main entry point for the Grocery List Planner application.
"""
from GroceryItem import GroceryItem
from ListManager import ListManager
from DataStore import DataStore
from categories import GROCERY_CATEGORIES, PRIORITY_LEVELS

class GroceryListApp:
    def __init__(self):
        self.list_manager = ListManager()
        self.data_store = DataStore()
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("        GROCERY LIST PLANNER")
        print("="*50)
        print("1. View Grocery List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item Quantity")
        print("5. Sort List")
        print("6. Save List")
        print("7. Load List")
        print("8. Export to Text File")
        print("9. Clear List")
        print("10. Show Categories")
        print("0. Exit")
        print("="*50)
    
    def view_list(self):
        """Display the current grocery list."""
        if not self.list_manager.items:
            print("\nYour grocery list is empty.")
            return
        
        print(f"\nGROCERY LIST ({self.list_manager.get_total_items()} items, total quantity: {self.list_manager.get_total_quantity()})")
        print("-" * 60)
        
        # Group by category
        summary = self.list_manager.get_category_summary()
        
        for category, items in summary.items():
            print(f"\n{category.upper()}:")
            print("-" * len(category))
            for item in items:
                print(f"  • {item}")
    
    def add_item_interactive(self):
        """Interactive method to add an item with validation."""
        print("\nADD NEW ITEM")
        print("-" * 20)
        
        name = input("Item name: ").strip()
        if not name:
            print("Error: Item name cannot be empty.")
            return
        
        try:
            quantity = int(input("Quantity: ").strip() or "1")
        except ValueError:
            print("Error: Quantity must be a number.")
            return
        
        print("\nAvailable categories:")
        for i, category in enumerate(GROCERY_CATEGORIES, 1):
            print(f"  {i}. {category}")
        
        try:
            cat_choice = int(input(f"\nSelect category (1-{len(GROCERY_CATEGORIES)}): ").strip() or "1")
            category = GROCERY_CATEGORIES[cat_choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection. Using default category.")
            category = GROCERY_CATEGORIES[0]
        
        print("\nPriority levels:")
        for i, priority in enumerate(PRIORITY_LEVELS, 1):
            print(f"  {i}. {priority}")
        
        try:
            pri_choice = int(input(f"\nSelect priority (1-{len(PRIORITY_LEVELS)}): ").strip() or "2")
            priority = PRIORITY_LEVELS[pri_choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection. Using medium priority.")
            priority = "Medium"
        
        success, message = self.list_manager.add_item(name, quantity, category, priority)
        print(message)
    
    def remove_item_interactive(self):
        """Interactive method to remove an item."""
        if not self.list_manager.items:
            print("The list is empty. Nothing to remove.")
            return
        
        item_name = input("Enter item name to remove: ").strip()
        if not item_name:
            print("Error: Please enter an item name.")
            return
        
        success, message = self.list_manager.remove_item(item_name)
        print(message)
    
    def update_quantity_interactive(self):
        """Interactive method to update item quantity."""
        if not self.list_manager.items:
            print("The list is empty. Nothing to update.")
            return
        
        item_name = input("Enter item name to update: ").strip()
        if not item_name:
            print("Error: Please enter an item name.")
            return
        
        try:
            new_quantity = int(input("Enter new quantity: ").strip())
        except ValueError:
            print("Error: Quantity must be a number.")
            return
        
        success, message = self.list_manager.update_quantity(item_name, new_quantity)
        print(message)
    
    def sort_list_interactive(self):
        """Interactive method to sort the list."""
        if not self.list_manager.items:
            print("The list is empty. Nothing to sort.")
            return
        
        print("\nSORT OPTIONS:")
        print("1. By Priority")
        print("2. By Category")
        print("3. By Name")
        
        choice = input("Select sort option (1-3): ").strip()
        
        if choice == "1":
            self.list_manager.sort_by_priority()
            print("List sorted by priority.")
        elif choice == "2":
            self.list_manager.sort_by_category()
            print("List sorted by category.")
        elif choice == "3":
            self.list_manager.sort_by_name()
            print("List sorted by name.")
        else:
            print("Invalid choice.")
    
    def show_categories(self):
        """Display available categories and priority levels."""
        print("\nAVAILABLE CATEGORIES:")
        for category in GROCERY_CATEGORIES:
            print(f"  • {category}")
        
        print("\nPRIORITY LEVELS:")
        for priority in PRIORITY_LEVELS:
            print(f"  • {priority}")
    
    def run(self):
        """Main application loop."""
        print("Welcome to Grocery List Planner!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-10): ").strip()
            
            if choice == "0":
                print("Thank you for using Grocery List Planner. Goodbye!")
                break
            elif choice == "1":
                self.view_list()
            elif choice == "2":
                self.add_item_interactive()
            elif choice == "3":
                self.remove_item_interactive()
            elif choice == "4":
                self.update_quantity_interactive()
            elif choice == "5":
                self.sort_list_interactive()
            elif choice == "6":
                success, message = self.data_store.save_list(self.list_manager)
                print(message)
            elif choice == "7":
                success, message = self.data_store.load_list(self.list_manager)
                print(message)
            elif choice == "8":
                filename = input("Enter filename (default: grocery_list.txt): ").strip() or "grocery_list.txt"
                success, message = self.data_store.export_to_text(self.list_manager, filename)
                print(message)
            elif choice == "9":
                success, message = self.list_manager.clear_list()
                print(message)
            elif choice == "10":
                self.show_categories()
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = GroceryListApp()
    app.run()