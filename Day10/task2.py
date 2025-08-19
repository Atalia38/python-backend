

from itertools import islice

def fibonacci():
    """Infinite Fibonacci generator: 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("First 12 Fibonacci numbers:")
    print(list(islice(fibonacci(), 12)))


    g = fibonacci()
    print("Next three:", next(g), next(g), next(g))
