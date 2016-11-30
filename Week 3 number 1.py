def reverse():
    '''
    Takes a string as input and reverses the order using extended slices

    returns the reversed string
    '''
    try:
    
        sentence=input("Please enter a sentence ")#1
        split1=sentence.split()#1

        for i in split1[::-1]:#extended slices. 3rd argument -1 reverses the sentence#n
            print (i)#n
    except Error:
        print('that is not the correct type of input')#1
reverse()    
    

#1+1+n+n+1=2n+3
#O(n)
