"""
Handles saving and loading grocery list data from JSON files.
"""
import json
import os
from GroceryItem import GroceryItem

class DataStore:
    def __init__(self, filename="grocery_list.json"):
        self.filename = filename
    
    def save_list(self, list_manager):
        """Save the grocery list to a JSON file."""
        try:
            data = {
                'items': [item.to_dict() for item in list_manager.items]
            }
            
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
            
            return True, f"Grocery list saved to {self.filename}"
        except Exception as e:
            return False, f"Error saving list: {e}"
    
    def load_list(self, list_manager):
        """Load the grocery list from a JSON file."""
        try:
            if not os.path.exists(self.filename):
                return False, f"File {self.filename} not found"
            
            with open(self.filename, 'r') as file:
                data = json.load(file)
            
            # Clear existing items and load new ones
            list_manager.clear_list()
            for item_data in data['items']:
                try:
                    item = GroceryItem.from_dict(item_data)
                    list_manager.items.append(item)
                except ValueError as e:
                    print(f"Warning: Skipping invalid item data: {e}")
            
            return True, f"Grocery list loaded from {self_filename}"
        except json.JSONDecodeError:
            return False, f"Error: {self.filename} contains invalid JSON"
        except Exception as e:
            return False, f"Error loading list: {e}"
    
    def export_to_text(self, list_manager, filename="grocery_list.txt"):
        """Export the grocery list to a readable text file."""
        try:
            with open(filename, 'w') as file:
                file.write("=== GROCERY LIST ===\n\n")
                
                # Group by category
                summary = list_manager.get_category_summary()
                
                if not summary:
                    file.write("No items in the list.\n")
                    return True, f"Exported empty list to {filename}"
                
                for category, items in summary.items():
                    file.write(f"\n{category.upper()}:\n")
                    file.write("-" * len(category) + "\n")
                    
                    for item in items:
                        file.write(f"  • {item.name} (Qty: {item.quantity}, Priority: {item.priority})\n")
                
                file.write(f"\nTotal items: {list_manager.get_total_items()}\n")
                file.write(f"Total quantity: {list_manager.get_total_quantity()}\n")
            
            return True, f"Grocery list exported to {filename}"
        except Exception as e:
            return False, f"Error exporting list: {e}"