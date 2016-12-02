def factorial():
    '''
    Takes a factorial number and counts the number of trailing zeroes
    Returns the number of trailing zeroes
    '''
    try:
        
        number=int(input("Please enter the factorial number you want to check for "))#1
        if number<5 and number>0:#1
            print('No trailing zeroes')#1
        elif number<0:#1
            error=ValueError('Number should be positive')#1
            raise error#1
        else:
            while number>=5:#n
                number=number//5#Keep dividing by 5 because what we are looking for is how many times the factorial divides by 5 and the powers of 5#n
                print(number)#n
    except ValueError:
        print("That is not a valid number/character")#1
factorial()
        
6+3n+1=3n+7
O(n)
