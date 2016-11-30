BINARY_SEARCH(value):
    size<-take in input for size of list
    numbers<-empty list to be searched through later
    range1<-start point of range
    range2<-end point of range
    r<-length from value of range1 to value of range2

    while length(numbers)<size:
        ask<-Take in list of numbers
        put the numbers into the empty list called numbers

    first<-0
    listSize<-length of list numbers
    last<-listSize


    while(first<=last):
        mid<-(first+last)//2

        if value=the middle value of the list numbers
            print "Value found"

            if that same value is in r
                print "Value whithin range"
                return True
            else
                print "Vaue not within range"
                return False
            return True

        else if value>the middle value of the list numbers
            first<-mid+1
        else if value<the middle value of the list numbers
            last<-mid-1
        else
            print "Value not found"
            return False
        
            
