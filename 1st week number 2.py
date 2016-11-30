def factorial():
    '''
    Takes a factorial number and counts the number of trailing zeroes
    Returns the number of trailing zeroes
    '''
    try:
        
        number=int(input("Please enter the factorial number you want to check for "))
        if number<5 and number>0:
            print('No trailing zeroes')
        elif number<0:
            error=ValueError('Number should be positive')
            raise error
        else:
            while number>=5:
                number=number//5#Keep dividing by 0 because what we are really looking for is how many times the factorial divides by 5 and the powers of 5
                print(number)
    except ValueError:
        print("That is not a valid number/character")
factorial()
        
