BINARY_SEARCH(value):
    size<-take in input for size of list
    numbers<-empty list to be searched through later
    range1<-start point of range
    range2<-end point of range
    r<-range from value of range1 to value of range2

    while length(numbers)<size:
        ask<-Take in list of numbers
        put the numbers into the empty list called numbers

    first<-0
    listSize<-length of list numbers
    last<-listSize

    found=False
    while(first<=last):
        mid<-(first+last)//2

        if the middle number from list numbers is in r
            then their is a value in the range
            found<-True
            break the while loop
        else if the middle number is lower than the first range1
            first<-mid+1
        else
            last<-mid-1

    if found:
        print('yes')
    else:
        print('no')
