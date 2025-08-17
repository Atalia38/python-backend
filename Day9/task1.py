

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi



class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"


class Dog(Animal):
    def speak(self) -> str:  
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:  
        return "Meow!"



class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner         
        self.__balance = float(balance) 

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



def make_it_speak(animals: list[Animal]) -> list[str]:
    """Works for any Animal subtype—each implements its own speak()."""
    return [f"{a.name}: {a.speak()}" for a in animals]

@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

    def __add__(self, other: "Vector2D"):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    
    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x:.1f}, y={self.y:.1f})"



class Notification(ABC):
    def __init__(self, to: str) -> None:
        self.to = to

    @abstractmethod
    def send(self, message: str) -> str:
        raise NotImplementedError


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
    return [n.send(message) for n in notifications]




class Shape(ABC):
    def __init__(self, color: str = "black") -> None:
    
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(color={self.color})"


class Circle(Shape):
    def __init__(self, radius: float, color: str = "black") -> None:
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
    def __init__(self, width: float, height: float, color: str = "black") -> None:
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError("width/height must be positive")
        self.__width = float(width)   
        self.__height = float(height) 

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def __repr__(self) -> str:
        return (
            f"Rectangle(width={self.__width:.2f}, height={self.__height:.2f}, "
            f"color={self.color!r})"
        )




def main() -> None:
    print("=" * 68)
    print("TOPICS DEMOS")
    print("=" * 68)

    
    dog, cat = Dog("Rex"), Cat("Luna")
    print("[Inheritance/Override]", dog, "->", dog.speak(), "|", cat, "->", cat.speak())


    acct = BankAccount("Faisal", 100)
    acct.deposit(50)
    
    acct.__balance = -999  
    print("[Encapsulation]", acct, "Visible balance:", acct.balance)


    print("[Polymorphism]")
    for line in make_it_speak([dog, cat, Animal("Thing")]):
        print("  ", line)


    v1, v2 = Vector2D(2, 3), Vector2D(4.5, -1)
    print("[Magic methods] v1:", v1, "| v2:", v2, "| v1 + v2 ->", v1 + v2)

    print("\n" + "=" * 68)
    print("HANDS-ON: Real-World Scenario — Notifications")
    print("=" * 68)

    sent = broadcast(
        [
            EmailNotification("user@example.com"),
            SMSNotification("+15551234567"),
            PushNotification("device-42"),
        ],
        "Order #A123 has shipped!",
    )
    for s in sent:
        print("  ", s)

    print("\n" + "=" * 68)
    print("EXERCISE: Shapes using OOP (Circle, Rectangle)")
    print("=" * 68)

    shapes: list[Shape] = [
        Circle(3, "red"),
        Rectangle(4, 6, "blue"),
        Circle(1.5, "green"),
    ]
    for s in shapes:
        print(f"  {s}: area={s.area():.2f}, perimeter={s.perimeter():.2f}")

    total_area = sum(s.area() for s in shapes)
    print(f"\n  Total area of all shapes: {total_area:.2f}")


if __name__ == "__main__":
    main()
