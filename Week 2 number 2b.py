number=int(input("Please enter the factorial number you want to check for "))#(1)
if number<5:#(1)
    print('No trailing zeroes')#(1)
else:#(1)
    while number>5:#(n)
        number=number//5#(n)
        print (number)#(1)
#1+1+1+1+n+n+1=2n+5
#O(n)
