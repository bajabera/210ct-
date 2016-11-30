def binary_search(value):
    '''
    Function that takes in one value to search for in a list

    Returns whether value was found and whether or not value was within a specific interval
    '''
    size=int(input("How long do you want the list to be? "))#size of list
    numbers=[]
    range1=int(input("Starting point of range"))
    range2=int(input("end point of range"))
    r=range(range1,range2)
    while len(numbers)<size:
        ask=int(input("Please enter a list of numbers "))
        numbers.append(ask)#to input numbers to a list
    first=0
    listSize=len(numbers)#calculates the size of list
    last=listSize

    while(first<=last):
        mid=(first+last)//2#calculates middle part of list

        if(value==numbers[mid]):#Checks if user value is equal to the middle value of the list
            print("Value found")
            
            if value in r:#Checks if value within range
                print("Value within range")
                return True
            else:
                print("Value not in range")
                return False
            return True
        
        elif(value>numbers[mid]):#Checks if user value is greater than the middle value of the vector
            first=mid+1#Increases the size of the first value
        elif(value<numbers[mid]):#Checks if user value is less than the middle value of the list
            last=mid-1#Reduces size of the last value
        else:
            print("Value not found")
            return False

    
binary_search(2)        

