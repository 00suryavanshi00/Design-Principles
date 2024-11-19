

class vehicle:

    def __init__(self, bodyType):

        self.bodyType = bodyType

# parent method is strict and every child has to override the method to implement this resulting in 
# code duplication
    def drive(self):

        print("I drive a simple vehicle")




class sportsVehicle(vehicle):

    def __init__(self,bodyType):

        vehicle.__init__(self, bodyType)


    def drive(self):
        
        print("I drive a sportscar")

    

class passengerVehicle(vehicle):

    def __init__(self,bodyType):

        vehicle.__init__(self, bodyType)


    def drive(self):
        
        print("I drive a passengerVehicle")




obj1 = vehicle('metal')
obj2 = sportsVehicle('plastic')

obj2.drive()