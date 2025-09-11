

import sqlite3
from datetime import datetime

DB_FILE = "finance.db"

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT CHECK(type IN ('income','expense')) NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a transaction
def add_transaction():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Salary, Groceries, Rent): ")
        t_type = input("Type (income/expense): ").strip().lower()
        if t_type not in ["income", "expense"]:
            print("❌ Invalid type. Must be 'income' or 'expense'.")
            return
        
        date_str = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
        date = date_str if date_str else datetime.today().strftime("%Y-%m-%d")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (amount, category, type, date) VALUES (?, ?, ?, ?)",
                        (amount, category, t_type, date))
        conn.commit()
        conn.close()
        print("✅ Transaction added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

# View all transactions
def view_transactions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, type, category, amount FROM transactions ORDER BY date")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No transactions found.")
        return
    
    print("\n--- Transactions ---")
    for row in rows:
        print(f"{row[0]}. {row[1]} | {row[2].capitalize()} | {row[3]} | ${row[4]:.2f}")

# Show financial summary
def financial_summary():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expenses = cursor.fetchone()[0] or 0
    conn.close()

    balance = income - expenses
    print("\n--- Financial Summary ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Net Balance: ${balance:.2f}")

# Main CLI Loop
def main():
    init_db()
    
    while True:
        print("\n--- Personal Finance Tracker (SQLite) ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Financial Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            financial_summary()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

