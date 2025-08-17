

from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from dataclasses import dataclass



print("="*72)
print("TOPICS DEMOS")
print("="*72)

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."  # generic sound

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

class Dog(Animal):
    def speak(self) -> str:  # override
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:  # override
        return "Meow!"

dog, cat = Dog("Rex"), Cat("Lama")
print("[Inheritance/Override]", dog, "->", dog.speak(), "|", cat, "->", cat.speak())







class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner               # public
        self.__balance = float(balance)  # private 

    @property
    def balance(self) -> float:
        """Read-only public view of the balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.__balance:
            raise ValueError("Invalid withdrawal amount")
        self.__balance -= amount

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.__balance:.2f})"

acct = BankAccount("Faisal", 100)
acct.deposit(50)
try:
    # Direct external writes to __balance are prevented (encapsulation)
    acct.__balance = -999  # creates a new attribute, does not change the real balance
except Exception as e:
    print("Attempt to set private balance failed:", e)
print("[Encapsulation]", acct, "Visible balance:", acct.balance)




def make_it_speak(animals: list[Animal]) -> list[str]:
    """Works for any Animal subtype—each implements its own speak()."""
    return [f"{a.name}: {a.speak()}" for a in animals]

lines = make_it_speak([dog, cat, Animal("Thing")])
print("[Polymorphism]")
for line in lines:
    print("  ", line)







    @dataclass(frozen=True)
    class Vector2D:
        x: float
        y: float

        def __add__(self, other):
            if not isinstance(other, Vector2D):
                return NotImplemented
            return Vector2D(self.x + other.x, self.y + other.y)

    # Optional: lets sum() start from 0 using a neutral element
    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

    def __repr__(self):
        return f"Vector2D(x={self.x:.1f}, y={self.y:.1f})"


class Notification(ABC):
    def __init__(self, to: str):
        self.to = to

    @abstractmethod
    def send(self, message: str) -> str:
        ...

class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email to {self.to}: {message}"

class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS to {self.to}: {message}"

class PushNotification(Notification):
    def send(self, message: str) -> str:
        return f"Push to {self.to}: {message}"


def broadcast(notifications: list[Notification], message: str) -> list[str]:
    # Polymorphism: each notification knows how to send itself
    return [n.send(message) for n in notifications]

sent = broadcast([EmailNotification("user@example.com"),
                    SMSNotification("+15551234567"),
                    PushNotification("device-42")],
                    "Order #A123 has shipped!")
for s in sent:
    print("  ", s)

print("\n" + "="*72)
print("EXERCISE: Shapes using OOP (Circle, Rectangle)")
print("="*72)


class Shape(ABC):
    def __init__(self, color: str = "black"):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(color={self.color})"

class Circle(Shape):
    def __init__(self, radius: float, color: str = "black"):
        super().__init__(color)
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.__radius = float(radius)  # private

    @property
    def radius(self) -> float:
        return self.__radius

    def area(self) -> float:
        return pi * self.__radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.__radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.__radius:.2f}, color={self.color!r})"

class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str = "black"):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError("width/height must be positive")
        self.__width = float(width)   # private
        self.__height = float(height) # private

    @property
    def width(self) -> float: return self.__width
    @property
    def height(self) -> float: return self.__height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def __repr__(self) -> str:
        return (f"Rectangle(width={self.__width:.2f}, height={self.__height:.2f}, "
                f"color={self.color!r})")

# Polymorphic processing of shapes
shapes: list[Shape] = [Circle(3, "red"), Rectangle(4, 6, "blue"), Circle(1.5, "green")]
for s in shapes:
    print(f"  {s}: area={s.area():.2f}, perimeter={s.perimeter():.2f}")

# Totals via polymorphism
total_area = sum(s.area() for s in shapes)
print(f"\n  Total area of all shapes: {total_area:.2f}")


if __name__ == "__main__":
    pass