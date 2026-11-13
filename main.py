from car import Car
from customer import Customer


Customer1=Customer("Jeje",21)
Customer2=Customer("Amy",22)

Car1=Car("Toyota","Red",500)
Car2=Car("Honda","Pink",200)

Customer1.rent(Car1)
print(Customer1.current_car == Car1)
print(Car1.renter == Customer1)
print(Customer2.rent(Car1))
print(Customer2.current_car)
print(Car1.renter == Customer1)
print(Customer1.rent(Car2))
print(Car1.renter==Customer1)
print(Car2.renter is None)
Customer1.drop()
print(Customer1.current_car)
print(Car1.renter is None)
Customer2.rent(Car1)
print(Customer2.current_car == Car1)
print(Car1.renter == Customer2)
print(Customer2.drop())
print(Customer2.current_car)
print(Customer2.drop())
print(Car1.renter is None)

# Customer2.rent(Car2)