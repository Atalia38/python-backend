


data = [5, 1, 7, 3, 9, 2]


sorted_data = sorted(data)
print("Sorted:", sorted_data)


filtered = [x for x in data if x % 2 == 1]
print("Filtered (odd numbers):", filtered)


transformed = [x**2 for x in data]
print("Transformed (squared):", transformed)