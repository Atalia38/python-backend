# mini_app.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Optional


def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = " ".join(p.capitalize() for p in name.strip().split())
    return f"Hello, {name or 'World'}!"


def fibonacci(n: int) -> int:
    """Return nth Fibonacci number (0-indexed)."""
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@dataclass
class Counter:
    value: int = 0
    on_change: Optional[Callable[[int], None]] = None  

    def _notify(self) -> None:
        if self.on_change:
            self.on_change(self.value)

    def inc(self, step: int = 1) -> None:
        if step <= 0:
            raise ValueError("step must be positive")
        self.value += step
        self._notify()

    def dec(self, step: int = 1) -> None:
        if step <= 0:
            raise ValueError("step must be positive")
        self.value -= step
        self._notify()
