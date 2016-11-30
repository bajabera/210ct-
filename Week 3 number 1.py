def reverse():
    '''
    Takes a string as input and reverses the order using extended slices

    returns the reversed string
    '''
    try:
    
        sentence=input("Please enter a sentence ")
        split1=sentence.split()

        for i in split1[::-1]:#extended slices. 3rd argument -1 reverses the sentence
            print (i)
    except Error:
        print('that is not the correct type of input')
reverse()    
    

