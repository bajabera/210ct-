def binary_search():
    '''
    Function that searches whether any value was found within a specific interval

    Returns whether value was found within a specific interval
    '''
    size=int(input("How long do you want the list to be? "))#size of list
    numbers=[]
    range1=int(input("Starting point of range"))
    range2=int(input("end point of range"))
    r=range(range1,range2)
    
    while len(numbers)<size:
        ask=int(input("Please enter a list of numbers "))
        numbers.append(ask)#to input numbers to a list
    numbers=sorted(numbers)
    print(numbers)
    first=0
    listSize=len(numbers)#calculates the size of list
    last=listSize
    found=False
    while(first<=last):
        mid=(first+last)//2#calculates middle part of list

        if numbers[mid] in r:
            found=True
            break

        elif numbers[mid]<range1:
            first=mid+1
        else:
            last=mid-1
    if found:
        print("yes value within the specific interval was found")
    else:
        print("no value found within interval")
      

    
binary_search()        

