

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name      
        self.breed = breed    

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."



dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "Husky")


print(dog1.describe())
print(dog2.describe())


dog1.species = "Canis lupus familiaris"


print("\nAfter modifying species for dog1:")
print(dog1.describe())  
print(dog2.describe())  
