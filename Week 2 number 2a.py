import random
def random_shuffle():
    '''
    Takes integer inputs from user and randomizes it
    '''
    try:
        ask1=int(input("How many numbers would you like in your list"))#input length of list#n
        max_list=ask1#1
        list1=[]#1
        while len(list1)<max_list:#n
            ask=input("enter number to create list")#gets the numbers of the list#n
            list1.append(int(ask))#n
    
        list2 = []#n
        while len(list1) > 0:#n
            index=random.choice(range(0,len(list1)))#n
            list2.append(list1.pop(index))#appends a randomly selected number using the index#n
        return list2#n
    except ValueError:
        print('Input a valid NUMBER!')#n
        
print(random_shuffle())


#n+1+1+n+n+n+n+n+n+n+n+n=10n+2
#O(n)


