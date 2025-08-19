

class Cycle:
    """
    Iterator that cycles through items for a fixed number of rounds.
    Example: Cycle(['A','B','C'], rounds=2) -> A B C A B C
    """
    def __init__(self, items, rounds=1):
        if rounds < 0:
            raise ValueError("rounds must be >= 0")
        self.items = list(items)
        self.rounds = rounds
        self._i = 0
        self._r = 0

    def __iter__(self):
        self._i = 0
        self._r = 0
        return self

    def __next__(self):
        if self._r >= self.rounds or not self.items:
            raise StopIteration
        val = self.items[self._i]
        self._i += 1
        if self._i >= len(self.items):
            self._i = 0
            self._r += 1
        return val


def sliding_window(iterable, size):
    """
    Generator that yields overlapping windows of length `size`.
    sliding_window([1,2,3,4], 3) -> (1,2,3), (2,3,4)
    """
    if size <= 0:
        raise ValueError("size must be >= 1")

    it = iter(iterable)
    from collections import deque
    window = deque(maxlen=size)

    for _ in range(size):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield tuple(window)

    for x in it:
        window.append(x)
        yield tuple(window)


if __name__ == "__main__":
    print("Cycle iterator:")
    for x in Cycle(["A", "B", "C"], rounds=2):
        print(x, end=" ")
    print("\n")

    print("Sliding-window generator:")
    for w in sliding_window([1,2,3,4,5,6], size=3):
        print(w)
