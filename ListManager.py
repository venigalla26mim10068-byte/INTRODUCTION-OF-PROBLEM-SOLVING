"""
Manages the grocery list with various operations and sorting capabilities.
"""
from GroceryItem import GroceryItem
from categories import GROCERY_CATEGORIES, PRIORITY_LEVELS

class ListManager:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, quantity=1, category=None, priority="Medium"):
        """Add a new item to the grocery list."""
        try:
            item = GroceryItem(name, quantity, category, priority)
            self.items.append(item)
            return True, f"Added: {item}"
        except ValueError as e:
            return False, f"Error: {e}"
    
    def remove_item(self, item_name):
        """Remove an item by name (case-insensitive partial match)."""
        original_count = len(self.items)
        self.items = [item for item in self.items if item_name.lower() not in item.name.lower()]
        removed_count = original_count - len(self.items)
        
        if removed_count > 0:
            return True, f"Removed {removed_count} item(s) containing '{item_name}'"
        else:
            return False, f"No items found containing '{item_name}'"
    
    def update_quantity(self, item_name, new_quantity):
        """Update the quantity of a specific item."""
        for item in self.items:
            if item_name.lower() in item.name.lower():
                try:
                    old_quantity = item.quantity
                    item.quantity = new_quantity
                    return True, f"Updated {item.name} quantity from {old_quantity} to {new_quantity}"
                except ValueError as e:
                    return False, f"Error: {e}"
        return False, f"Item '{item_name}' not found"
    
    def sort_by_priority(self):
        """Sort items by priority level."""
        priority_order = {level: idx for idx, level in enumerate(PRIORITY_LEVELS)}
        self.items.sort(key=lambda x: priority_order[x.priority])
    
    def sort_by_category(self):
        """Sort items by category."""
        category_order = {category: idx for idx, category in enumerate(GROCERY_CATEGORIES)}
        self.items.sort(key=lambda x: category_order[x.category])
    
    def sort_by_name(self):
        """Sort items alphabetically by name."""
        self.items.sort(key=lambda x: x.name.lower())
    
    def get_items_by_category(self, category):
        """Get all items in a specific category."""
        return [item for item in self.items if item.category == category]
    
    def get_items_by_priority(self, priority):
        """Get all items with a specific priority."""
        return [item for item in self.items if item.priority == priority]
    
    def get_category_summary(self):
        """Get a summary of items by category."""
        summary = {}
        for category in GROCERY_CATEGORIES:
            category_items = self.get_items_by_category(category)
            if category_items:
                summary[category] = category_items
        return summary
    
    def clear_list(self):
        """Clear all items from the list."""
        self.items.clear()
        return True, "Grocery list cleared"
    
    def get_total_items(self):
        """Get the total number of items in the list."""
        return len(self.items)
    
    def get_total_quantity(self):
        """Get the total quantity of all items."""
        return sum(item.quantity for item in self.items)