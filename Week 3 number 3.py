

vowels="aeiou"#string of vowels

def remove_vowel(a):
    '''
    recursive function that removes vowels from a string
    '''
    x=a.lower()#makes sure all input is lower case
    if not x:
        return x#base case
    elif x[0] in vowels:#if first element in list vowels
        return remove_vowel(x[1:])#slice first element, moves onto the next
    else:
        return x[0]+remove_vowel(x[1:])

print(remove_vowel("Excessive work"))




###Pseudo code
##vowels<-"aeiouAEIOU"
##REMOVE_VOWEL(x)
##    if not x
##        return x
##    else if x[0] in vowels
##        return REMOVE_VOWEL(x[1:])
##    else
##        return x[0]+REMOVE_VOWEL(x[1:])
