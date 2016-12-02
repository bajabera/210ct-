INPUT MATRIX
m<-(Matrix as a list)#1
n<-(Matrix as a list)#1
p<-(product Matrix as a list)#1

MATRIX ADDITION(m,n)
     for i 1<- to length(m)#n
         m[i]+n[i]
     return p[i]#n
SUBTRACTION(m,n)
     for i 1<- to lenth(m)#n
         m[i]-n[i]
     return p[i]#n
MATRIX MULTIPLICATION(m,n)
//Takes 2 matrices as input and multiplies each row by corresponding column
     for each row value of m#n
         for each column value of n#n*n
             for position in final matrix#n*n*n
                 p[i]=(m[i]*n[i])+(m[i+1]*n[i+size of matrix])
    return p#n

MULTIPLY BY INTEGER(x,p)
//Takes an integer "x" and multiplies by a matrix "p"
    for i in p#n
        x*p[i]#n

FORMULA
    #A=B*C-2*(B+C)
    D<-MATRIX MULTIPLICATION(B,C)
    E<-MATRIX ADDITION(B,C)
    F<-MULTIPLY BY INTEGER(2,E)
    A<-D-FE
#1+1+1+n+n+n+n+n+n^2+n^3+n+n+n=3+8n+n^2+n^3
    #O(n^3)
