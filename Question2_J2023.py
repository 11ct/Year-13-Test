ID = ""
MaxSpeed = 0
CurrentSpeed = 0
IncreaseAmount = 0
HorizontalPosition = 0


class Vehicles:
    def __init__(self, ID, MaxSpeed, IncreaseAmount, CurrentSpeed = 0, HorizontalPosition = 0):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = CurrentSpeed
        self.__HorizontalPosition = HorizontalPosition
    
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def IncreaseAmount(self):
        return self.__IncreaseAmount
    
    def HorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, CurrentSpeed):
        self.__CurrentSpeed = CurrentSpeed
    
    def SetHorizontalPosition(self, HorizontalPosition):
        self.__HorizontalPosition = HorizontalPosition
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        self.__HorizontalPosition += self.__CurrentSpeed
        if self.__CurrentSpeed > self.__MaxSpeed:
            print("Invalid, exceeds max speed of the vehicle.")

Vehicle = Vehicles()


class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, MaxHeight, VerticalChange = 0):
        super().__init__(ID, MaxSpeed, IncreaseAmount, CurrentSpeed, HorizontalPosition)
        self.__MaxHeight = MaxHeight
        self.__VerticalChange = VerticalChange
        self.__VerticalPostion = 0

    def IncreseSpeed(self):
        global VerticalPosition, HorizontalPosition
        self.__VerticalPostion += self.__VerticalChange
        self.__CurrentSpeed += self.__IncreaseAmount
        self.__HorizontalPosition += self.__CurrentSpeed
        if self.__VerticalPostion > self.__MaxHeight:
            print("Invalid, exceeds max height of the helicopter.")
        if self.__CurrentSpeed > self.__MaxSpeed:
            print("Invalid, exceeds max speed of the helicopter.")

def Output(self):
    global VerticalPosition
    HorizontalPosition = self.__HorizontalPosition
    CurrentSpeed = self.__CurrentSpeed
    VerticalPosition = self.__VerticalPostion
    OutputHorizontal = print("The current horizontal position of the vehicle is", HorizontalPosition)
    OutputCurrentSpeed = print("The current speed of the vehicle is", CurrentSpeed)
    OutputVertical = print("The current vertical position of the vehicle is", VerticalPosition)
    return OutputHorizontal, OutputVertical, OutputCurrentSpeed

Helicopters = Helicopter()

def main():
    NewCar = Vehicles("Tiger", 100, 20)
    NewCar.IncreaseSpeed()
    NewCar.IncreaseSpeed()
    NewCar.Output()
    
    NewHelicopter = Helicopter("Lion", 350, 40, 100, 3)
    NewHelicopter.IncreaseSpeed()
    NewHelicopter.IncreaseSpeed()






    



    
    