

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Iterable, Optional




class Dog:

    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
    
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} says woof!"

    @classmethod
    def set_species(cls, new_species: str) -> None:
        cls.species = new_species

    
    @staticmethod
    def dog_years(human_years: int) -> int:
        return human_years * 7




class InsufficientFunds(Exception):
    pass



#Hands On
class BankAccount:
    bank_name = "Python National Bank"  

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner                  
        self._balance = float(balance)      

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        self._require_positive(amount, "deposit")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._require_positive(amount, "withdrawal")
        if amount > self._balance:
            raise InsufficientFunds(
                f"Withdrawal {amount:.2f} exceeds balance {self._balance:.2f}"
            )
        self._balance -= amount

    def transfer_to(self, other: "BankAccount", amount: float) -> None:
        """Atomic transfer using withdraw+deposit."""
        self.withdraw(amount)
        other.deposit(amount)

    @staticmethod
    def _require_positive(amount: float, label: str) -> None:
        if amount <= 0:
            raise ValueError(f"{label.capitalize()} amount must be positive.")

    @classmethod
    def rename_bank(cls, new_name: str) -> None:
        cls.bank_name = new_name

    def __repr__(self) -> str:
        return f"<{self.bank_name} | {self.owner}: ${self._balance:.2f}>"




class NotAvailableError(Exception):
    pass


#Exercise

@dataclass
class Book:
    title: str
    author: str
    copies_total: int
    id: int = field(init=False)
    copies_available: int = field(init=False)

    # class variable to auto-assign IDs
    _next_id: int = 1

    def __post_init__(self):
        if self.copies_total < 1:
            raise ValueError("A book must have at least 1 copy.")
        self.copies_available = self.copies_total
        self.id = Book._next_id
        Book._next_id += 1

    def checkout(self) -> None:
        if self.copies_available <= 0:
            raise NotAvailableError(f"'{self.title}' is not available.")
        self.copies_available -= 1

    def checkin(self) -> None:
        if self.copies_available < self.copies_total:
            self.copies_available += 1

    @property
    def is_available(self) -> bool:
        return self.copies_available > 0

    def __repr__(self) -> str:
        return f"[{self.id}] {self.title} — {self.author} (avail {self.copies_available}/{self.copies_total})"


@dataclass
class Member:
    name: str
    id: int
    borrowed_book_ids: List[int] = field(default_factory=list)

    max_books: int = 3

    def can_borrow(self) -> bool:
        return len(self.borrowed_book_ids) < Member.max_books


class Library:
    def __init__(self, name: str):
        self.name = name
        self._books: Dict[int, Book] = {}
        self._members: Dict[int, Member] = {}


    def add_book(self, title: str, author: str, copies: int = 1) -> Book:
        book = Book(title=title, author=author, copies_total=copies)
        self._books[book.id] = book
        return book

    def register_member(self, name: str) -> Member:
        new_id = 1 + max(self._members.keys(), default=0)
        member = Member(name=name, id=new_id)
        self._members[member.id] = member
        return member


    def find_books(self, query: str) -> List[Book]:
        q = query.strip().lower()
        return [
            b for b in self._books.values()
            if q in b.title.lower() or q in b.author.lower()
        ]

    def get_book(self, book_id: int) -> Book:
        return self._books[book_id]

    def get_member(self, member_id: int) -> Member:
        return self._members[member_id]

    # -- Circulation --
    def checkout(self, member_id: int, book_id: int) -> None:
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if not member.can_borrow():
            raise NotAvailableError(f"{member.name} has reached the borrow limit ({Member.max_books}).")
        book.checkout()
        member.borrowed_book_ids.append(book_id)

    def checkin(self, member_id: int, book_id: int) -> None:
        member = self.get_member(member_id)
        book = self.get_book(book_id)
        if book_id in member.borrowed_book_ids:
            member.borrowed_book_ids.remove(book_id)
            book.checkin()

    def inventory(self) -> Iterable[str]:
        for book in sorted(self._books.values(), key=lambda b: b.id):
            yield repr(book)

    def member_status(self, member_id: int) -> str:
        m = self.get_member(member_id)
        titles = [self._books[b].title for b in m.borrowed_book_ids]
        return f"{m.name} (ID {m.id}) has {len(titles)} book(s): {', '.join(titles) or '—'}"




if __name__ == "__main__":
    print("=== Topics Demo ===")
    d = Dog("Bolt", 4)
    print(d.speak())
    print("Species:", Dog.species)
    Dog.set_species("Goodest Pupper")
    print("New species (class var changed):", Dog.species)
    print("Dog years for 4:", Dog.dog_years(4))
    print()

    print("=== Hands-on: BankAccount ===")
    a = BankAccount("Alice", 200)
    b = BankAccount("Bob", 50)
    print(a, b)
    a.deposit(100)
    b.withdraw(20)
    a.transfer_to(b, 50)
    print("After transactions:", a, b)
    BankAccount.rename_bank("PyBank Intl.")
    print("Renamed bank shows on all accounts:", a, b)
    print()

    print("=== Exercise: Library System ===")
    lib = Library("Central Library")
    bk1 = lib.add_book("Clean Code", "Robert C. Martin", copies=2)
    bk2 = lib.add_book("The Pragmatic Programmer", "Andrew Hunt", copies=1)
    bk3 = lib.add_book("Python Tricks", "Dan Bader", copies=3)

    mem1 = lib.register_member("Atalia")
    mem2 = lib.register_member("Ahmad")

    
    print("Search 'python':", lib.find_books("python"))


    lib.checkout(mem1.id, bk1.id)
    lib.checkout(mem2.id, bk1.id)          
    try:
        lib.checkout(mem1.id, bk1.id)      
    except NotAvailableError as e:
        print("Checkout blocked:", e)

    
    lib.checkin(mem2.id, bk1.id)
    lib.checkout(mem1.id, bk1.id)           


    print("\nInventory:")
    for line in lib.inventory():
        print(" ", line)
    print(lib.member_status(mem1.id))
    print(lib.member_status(mem2.id))
