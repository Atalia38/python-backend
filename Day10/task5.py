

from itertools import islice
from math import isqrt

def primes():
    """
    Infinite prime generator using incremental trial division.
    Reuses previously found primes and stops testing at sqrt(n).
    """
    found = []        
    n = 2
    while True:
        is_prime = True
        limit = isqrt(n)
        for p in found:
            if p > limit:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            found.append(n)
            yield n
        n += 1


if __name__ == "__main__":
    print("First 20 primes:")
    print(list(islice(primes(), 20)))


    g = primes()
    print("Next five primes after the first 10:")
    _ = list(islice(g, 10))  # skip 10
    print([next(g) for _ in range(5)])
