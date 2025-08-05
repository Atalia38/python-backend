

def second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

nums = [5, 3, 9, 1, 9]
print("Second-largest number:", second_largest(nums))
