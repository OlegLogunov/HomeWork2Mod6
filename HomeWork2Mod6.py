class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self, horse_power):
        self.horse_power = horse_power
        print(f"Мощность автомобиля {self.horse_power} л.с.")
        return self.horse_power


class Nissan(Car, Vehicle):
    Car.price = 1500000
    Vehicle.vehicle_type = "Nissan"

    def horse_powers(self):
        super().horse_powers(180)


my_car = Car()
my_car.horse_powers(150)

my_nissan = Nissan()
print(Nissan.vehicle_type, Nissan.price)
my_nissan.horse_powers()
