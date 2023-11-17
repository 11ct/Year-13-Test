global Animal, Colour
Animal = [] #Contain 20 elements
Colour = [] #Contain 10 elements


AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DTP):
    global AnimalTopPointer, ColourTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DTP)
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global AnimalTopPointer, ReturnData
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData
    
def ReadData():
    global AnimalTopPointer, ColourTopPointer
    RAnimals = open("AnimalData.txt", "r")
    for thisline in RAnimals:
        PushAnimal(thisline)
    RAnimals.close()

def PushColour(CTP):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = CTP
        ColourTopPointer += 1
        return True
    
def PopColour():
    global ColourTopPointer, ReturnData1
    ReturnData1 = 0
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData1 = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData1


def ReadData1():
    try:
        RAnimals = open("AnimalData.txt", "r")
        for line in RAnimals:
            PushAnimal(line.strip())
        RAnimals.close()
    except IOError:
        print("Please check if the file exists")

    try:  
        RColours = open("ColourData.txt", "r")
        for line1 in RColours:
            PushColour(line1.strip())
        RColours.close()
    except IOError:
        print("Please check if the file exists")

def OutputItem():
    global AnimalTopPointer, ColourTopPointer
    CurrentColour = PopColour(Colour)
    CurrentAnimal = PopAnimal(Animal)
    if CurrentColour == "":
        print("No colour")
        PushAnimal(CurrentAnimal)
    else:
        if CurrentAnimal == "":
            print("No animal")
            PushColour(CurrentColour)
        else:
            print(CurrentColour + " " + CurrentAnimal)

def MainProgram():
    global AnimalTopPointer, ColourTopPointer
    ReadData1()
    for x in range(4):
        OutputItem()

MainProgram()