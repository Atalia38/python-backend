# exercise1_fibonacci

class Fibonacci:
    """Iterates the Fibonacci sequence up to n terms (0-indexed start: 0, 1, 1, 2, ...)."""
    def __init__(self, n):
        if n < 0:
            raise ValueError("n must be >= 0")
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):

        self.i = 0
        self.a, self.b = 0, 1
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
    
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        return val


if __name__ == "__main__":
    print(list(Fibonacci(10))) 







    # exercise2_alternating_signs

def alternating_signs(nums):
    """
    Yields each number with alternating signs: +, -, +, -, ...
    Uses absolute values so the pattern is guaranteed.
    """
    sign = 1
    for n in nums:
        yield sign * abs(n)
        sign *= -1


if __name__ == "__main__":
    data = [3, 7, 0, 4, 9]
    print(list(alternating_signs(data)))  







    # exercise3_word_char_ascii

def word_char_ascii(words):
    """Return {word: {char: ord(char) for char in word}} for each word."""
    return {w: {ch: ord(ch) for ch in w} for w in words}


if __name__ == "__main__":
    words = ["hi", "abc", "Zoo"]
    print(word_char_ascii(words))





    # exercise4_uppercase_vowels

def uppercase_vowels(s):
    """Return a set of uppercase vowels present in s."""
    vowels = "aeiou"
    return {ch.upper() for ch in s if ch.lower() in vowels}


if __name__ == "__main__":
    s = "Beautiful, curious code!"
    print(uppercase_vowels(s))  











    # exercise5_primes_generator

from math import isqrt

def primes():
    """
    Infinite generator of prime numbers in ascending order.
    Uses trial division by previously found primes up to sqrt(n).
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
    g = primes()
    first_six = [next(g) for _ in range(6)]
    print(first_six)  


    


