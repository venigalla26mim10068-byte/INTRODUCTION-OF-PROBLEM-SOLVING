"""
Defines the GroceryItem class with validation and display methods.
"""
from categories import GROCERY_CATEGORIES, PRIORITY_LEVELS

class GroceryItem:
    def __init__(self, name, quantity=1, category=None, priority="Medium"):
        self.name = name
        self.quantity = quantity
        self.category = category if category else GROCERY_CATEGORIES[0]
        self.priority = priority
        
        self._validate_item()
    
    def _validate_item(self):
        """Validate item attributes."""
        if not self.name or not self.name.strip():
            raise ValueError("Item name cannot be empty")
        
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if self.category not in GROCERY_CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(GROCERY_CATEGORIES)}")
        
        if self.priority not in PRIORITY_LEVELS:
            raise ValueError(f"Priority must be one of: {', '.join(PRIORITY_LEVELS)}")
    
    def to_dict(self):
        """Convert item to dictionary for serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'category': self.category,
            'priority': self.priority
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create item from dictionary."""
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            category=data['category'],
            priority=data['priority']
        )
    
    def __str__(self):
        return f"{self.name} (Qty: {self.quantity}, Category: {self.category}, Priority: {self.priority})"
    
    def __repr__(self):
        return f"GroceryItem(name='{self.name}', quantity={self.quantity}, category='{self.category}', priority='{self.priority}')"