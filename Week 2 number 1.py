def perfect_square(x):
    '''
    takes a number as an argument and returns the highest perfect square
    '''

    sqrt=x**(1/2)
    if sqrt.is_integer():
        print(x)
    else:
        perfect_square(x-1)

perfect_square(50)

##Pseudocode
##
##PERFECT SQUARE(x)
##    sqrt<-x**1/2
##    if sqrt is an integer
##        print x
##    else
##        PERFECT SQUARE(X-1)
