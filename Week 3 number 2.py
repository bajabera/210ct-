def prime(x,y):
    '''
    takes in the number you want to search for and the number directly below it
    y is decremented until 2 to see if x is a prime number
    
    '''
    try:
        if x<=1:
            print("not prime")  
        if y<2:#base case. The divisor is decremented till it goes to less than 2 to see if any number below x is divisible by it
            print ("prime")    
        else:
            if x%y==0:#if its divisible by a number below it then it's not a prime number
                print("not prime")
            else:
                prime(x,y-1)
    except ValueError:
        print('that is not a valid number')
        
prime(347,346)


##PRIME(x,y)
##    if x<=1
##        return false
##    if y<2
##        return true
##    else
##        if x/y has no remainders
##            return false
##        else
##            PRIME(x,y-1)
