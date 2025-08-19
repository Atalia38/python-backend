

def demo_comprehensions(nums):

    list_comp = [n*n for n in nums if n % 2 == 0]


    dict_comp = {n: n*n for n in nums if n % 2 == 1}


    set_comp = {(n*n) % 10 for n in nums}

    return list_comp, dict_comp, set_comp


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    lst, dct, st = demo_comprehensions(data)
    print("List comprehension (even squares):", lst)
    print("Dict comprehension (odd -> square):", dct)
    print("Set comprehension (unique last digits of squares):", st)
