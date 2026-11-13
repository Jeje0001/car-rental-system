class Customer:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.current_car=None

    def rent(self,car):

        if car.renter is None and self.current_car is None:
            self.current_car=car
            car.renter=self
            return
        if car.renter is not None:
            return f"The car is currently being rented"

        if self.current_car is not None:
            return f"You can not rent this car"

    def drop(self):
        if self.current_car == None:
            return f"You haven't rented any car"

        self.current_car.renter=None

        self.current_car=None
