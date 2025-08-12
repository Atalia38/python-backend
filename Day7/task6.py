


class Car:

    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1  

    def display_car(self):
        return f"Car: {self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars



car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
car4= Car("ttt","hhhhh")

print(car1.display_car())
print(car2.display_car())
print(car3.display_car())
print(car4.display_car())

print(f"Total cars created: {Car.get_total_cars()}")
