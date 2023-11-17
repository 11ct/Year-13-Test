DataArray = [] #To store 25 integers


def PrintArray(array):
    for y in array:
        print(y, end=" ")
    
def LinearSearch(Array, Input):
    global count
    count = 0
    for i in Array:
        if int(i) == Input:
            count += 1
    return count


def main():
    RDataArray = open("Data.txt", "r")
    for x in RDataArray:
        DataArray.append(x.strip())

    UserInput = int(input("Please enter an integer between 0 and 100 inclusive:"))
    while UserInput <0 or UserInput >100:
        UserInput = int(input("Please enter an integer between 0 and 100 inclusive:"))

    
    LinearSearch(DataArray, UserInput)
    print("The number", UserInput, "is found", count, "times")
    
    PrintArray(DataArray)
    
    
    RDataArray.close()

main()









