


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."



person1 = Person("Atalia", 22)
person2 = Person("Ahmad", 30)


print(person1.introduce())
print(person2.introduce())
