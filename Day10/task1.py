

class Range:
    """
    Simple inclusive range: Range(start, end, step=1)
    Implements the iterator protocol (__iter__, __next__).
    """
    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError("step cannot be 0")
        self.start = start
        self.end = end
        self.step = step
        self._cur = start
        self._asc = step > 0

    def __iter__(self):
    
        self._cur = self.start
        return self

    def __next__(self):
        if (self._asc and self._cur > self.end) or (not self._asc and self._cur < self.end):
            raise StopIteration
        val = self._cur
        self._cur += self.step
        return val


if __name__ == "__main__":

    xs = [10, 20, 30, 40]
    it = iter(xs)              
    print("Manual iteration over list:")
    try:
        while True:
            print(next(it), end=" ")
    except StopIteration:
        print("\n(end)\n")

    print("Custom Range iterable:")
    for n in Range(1, 10, 2):
        print(n, end=" ")
    print("\nDescending Range:")
    for n in Range(10, 1, -3):
        print(n, end=" ")
    print()
