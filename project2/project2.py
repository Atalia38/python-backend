

import sqlite3

DB_FILE = "ecommerce.db"

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )
    """)

    # Preload products if table is empty
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        products = [
            ("Laptop", 1200.00, 5),
            ("Smartphone", 800.00, 10),
            ("Headphones", 150.00, 20),
            ("Book: Python Programming", 40.00, 15),
            ("Gaming Mouse", 60.00, 8),
        ]
        cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products)
        print("📦 Preloaded default products into store.")

    conn.commit()
    conn.close()


# ---------- CLASSES ----------
class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self._stock = stock  # Encapsulation

    def reduce_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        return False

    def get_stock(self):
        return self._stock


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.cart = ShoppingCart(self)


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity):
        if product.get_stock() >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            print(f"✅ Added {quantity} x {product.name} to cart.")
        else:
            print("❌ Not enough stock!")

    def view_cart(self):
        if not self.items:
            print("🛒 Cart is empty.")
            return
        print("\n--- Shopping Cart ---")
        total = 0
        for product, qty in self.items.items():
            subtotal = product.price * qty
            print(f"{product.name} x {qty} = ${subtotal:.2f}")
            total += subtotal
        print(f"Total: ${total:.2f}")

    def checkout(self):
        if not self.items:
            print("❌ Cart is empty.")
            return

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        total = 0
        for product, qty in self.items.items():
            if product.reduce_stock(qty):
                subtotal = product.price * qty
                total += subtotal
                cursor.execute("UPDATE products SET stock=? WHERE id=?", (product.get_stock(), product.id))
            else:
                print(f"❌ Not enough stock for {product.name}. Skipping.")

        conn.commit()
        conn.close()

        print(f"✅ Checkout complete! Total: ${total:.2f}")
        self.items.clear()


# ---------- DATABASE OPERATIONS ----------
def get_all_products():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return [Product(*row) for row in rows]


def add_user(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()


def get_user(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None


# ---------- MAIN CLI ----------
def main():
    init_db()

    print("=== Simple E-commerce Store Backend ===")
    username = input("Enter your username: ")
    add_user(username)
    user = get_user(username)

    while True:
        print("\n--- Menu ---")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            products = get_all_products()
            print("\n--- Available Products ---")
            for p in products:
                print(f"{p.id}. {p.name} - ${p.price:.2f} (Stock: {p.get_stock()})")

        elif choice == "2":
            products = get_all_products()
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            product = next((p for p in products if p.id == product_id), None)
            if product:
                user.cart.add_product(product, quantity)
            else:
                print("❌ Product not found.")

        elif choice == "3":
            user.cart.view_cart()

        elif choice == "4":
            user.cart.checkout()

        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
