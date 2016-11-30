import random
def random_shuffle():
    '''
    Takes integer inputs from user and randomizes it
    '''
    try:
        ask1=int(input("How many numbers would you like in your list"))#input length of list
        max_list=ask1
        list1=[]
        while len(list1)<max_list:
            ask=input("enter number to create list")#gets the numbers of the list
            list1.append(int(ask))
    
        list2 = []
        while len(list1) > 0:
            index=random.choice(range(0,len(list1)))
            list2.append(list1.pop(index))#appends a randomly selected number using the index
        return list2
    except ValueError:
        print('Input a valid NUMBER!')
        
print(random_shuffle())
