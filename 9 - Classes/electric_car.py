class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year}, {self.make}, {self.model}"
        print(f"{long_name.title()}")

    def read_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """Describes the battery of an electric car."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print the range provided by the battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car has a range of {range}km on a full charge.")

    def upgrade_battery(self):
        """Upgrades the battery to 100kwH"""
        print(f"\nUpgrading battery size...")
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"The battery size has been upgraded to {self.battery_size}kWh!")
        else:
            print(
                f"The battery size is already at {self.battery_size}kWh. No need to ugprade!"
            )


class ElectricCar(Car):
    """Represents aspects of a car, specific to an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initializes attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


myTesla = ElectricCar("tesla", "model x", 2020)
myTesla.get_descriptive_name()
myTesla.battery.describe_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()