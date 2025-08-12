

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        """Return formatted string of the menu item."""
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []  

    def add_item(self, item):
        """Add a MenuItem object to the order."""
        self.items.append(item)
        print(f"Added {item.name} to order.")

    def remove_item(self, name):
        """Remove a MenuItem by name."""
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed {item.name} from order.")
                return
        print(f"Item '{name}' not found in order.")

    def calculate_total(self):
        """Calculate and return the total price."""
        return sum(item.price for item in self.items)

    def display_order(self):
        """Show all items and total."""
        if not self.items:
            print("Order is empty.")
            return
        print("\nYour Order:")
        for item in self.items:
            print(item.display())
        print(f"Total: ${self.calculate_total():.2f}")




item1 = MenuItem("Spring Rolls", 5.99, "Appetizer")
item2 = MenuItem("Grilled Chicken", 12.50, "Main Course")
item3 = MenuItem("Cheesecake", 6.75, "Dessert")


order = Order()


order.add_item(item1)
order.add_item(item2)
order.add_item(item3)


order.display_order()


order.remove_item("Grilled Chicken")


order.display_order()
