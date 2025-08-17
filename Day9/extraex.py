

"""task1"""

from typing import Callable

def make_multiplier(base: int) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        
        return x * x if base == 0 else base * x
    return multiply


if __name__ == "__main__":
    doubler = make_multiplier(2)
    tripler = make_multiplier(3)
    squarer = make_multiplier(0)  

    print("doubler(7)  ->", doubler(7))   
    print("tripler(5)  ->", tripler(5))   
    print("squarer(11) ->", squarer(11)) 



"""task2"""


from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


if __name__ == "__main__":
    @count_calls
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    print(greet("Faisal"))
    print(greet("Sara"))
    print(greet("Atalia"))
    print("greet.calls ->", greet.calls)  



    """task3"""


from functools import wraps
from numbers import Real

def require_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def check(value, name):
            if isinstance(value, Real):
                if value <= 0:
                    raise ValueError(f"Argument '{name}' must be > 0 (got {value})")
    
        for idx, v in enumerate(args, start=1):
            check(v, f"arg{idx}")
    
        for k, v in kwargs.items():
            check(v, k)
        return func(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    @require_positive
    def area_of_rectangle(width: float, height: float) -> float:
        return width * height

    print("area_of_rectangle(4, 6) ->", area_of_rectangle(4, 6))  

    try:
        area_of_rectangle(width=5, height=0) 
    except ValueError as e:
        print("Error:", e)

