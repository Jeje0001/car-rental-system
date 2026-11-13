class Car:

    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        self.renter=None
    

    def display(self):
        print(f"The name of the car is {self.name}")
        print(f"The color of the car is {self.color}")
        print(f"The Price of the car is {self.price}")
        if self.renter is None:
            print("The car is available for rent")
        else:
            print(f"The car is currently rented by {self.renter.name}")