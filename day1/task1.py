bill = float(input("Enter the total bill:"))
tip_percent = float(input("Enter the tip"))

tip = bill*(tip_percent / 100)
total= bill + tip

print(f"Tip: {tip}")
print(f"total: {total}")

