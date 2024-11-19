

class DriveStrategy:
    def drive(self):
        raise NotImplementedError("Drive method should be implemented by subclasses")

# Concrete strategy classes for different driving behaviors
class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        return "Driving with normal strategy"

class AggressiveDriveStrategy(DriveStrategy):
    def drive(self):
        return "Driving with aggressive strategy"

class EcoDriveStrategy(DriveStrategy):
    def drive(self):
        return "Driving with eco strategy"


class vehicle:



    def __init__(self, bodyType, driveStrategy : DriveStrategy):

        self.bodyType = bodyType
        self.driveStrategy = driveStrategy



class sportsVehicle(vehicle):

    def __init__(self, bodyType, speed, driveStrategy):

        self.speed = speed
        
        vehicle.__init__(self, bodyType, driveStrategy)


class passengerVehicle(vehicle):

    def __init__(self, bodyType, load, driveStrategy):

        self.load = load
        vehicle.__init__(self, bodyType, driveStrategy)



ferari = sportsVehicle('plastic', '100kms', driveStrategy=AggressiveDriveStrategy())

print(ferari.driveStrategy.drive())




    