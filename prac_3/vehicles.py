"""Пример полиморфизма для разных транспортных средств."""

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def describe(self):
        return f"Транспорт {self.brand}, скорость до {self.max_speed} км/ч."


class Car(Vehicle):
    def __init__(self, brand, max_speed, doors=4):
        super().__init__(brand, max_speed)
        self.doors = doors

    def describe(self):
        return f"Автомобиль {self.brand}: {self.doors} двери, до {self.max_speed} км/ч."


class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, has_electric_motor=False):
        super().__init__(brand, max_speed)
        self.has_electric_motor = has_electric_motor

    def describe(self):
        motor = "электрический" if self.has_electric_motor else "обычный"
        return f"{motor.capitalize()} велосипед {self.brand}: до {self.max_speed} км/ч."


class Airplane(Vehicle):
    def __init__(self, brand, max_speed, passenger_capacity):
        super().__init__(brand, max_speed)
        self.passenger_capacity = passenger_capacity

    def describe(self):
        return (
            f"Самолёт {self.brand}: {self.passenger_capacity} пассажиров, "
            f"до {self.max_speed} км/ч."
        )


if __name__ == "__main__":
    vehicles = [
        Car("Toyota", 180),
        Bicycle("Trek", 35),
        Airplane("Airbus A320", 840, 180),
    ]
    for vehicle in vehicles:
        print(vehicle.describe())
