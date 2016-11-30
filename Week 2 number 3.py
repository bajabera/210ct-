INPUT MATRIX
m<-(Matrix as a list)#1
n<-(Matrix as a list)#1
p<-(product Matrix)#1

MATRIX ADDITION(m,n)
    m[i]+n[i] for i 1<- to length(m)# 

SUBTRACTION(m,n)
    m[i]-n[i] for i 1<- to lenth(m)

MATRIX MULTIPLICATION(m,n)
//Takes 2 matrices as input and multiplies each row by corresponding column
     for each row value of m#n
         for each column value of n#n*n
             for position in final matrix#n*n*n
                 p[i]=(a[i]*b[i])+(a[i+1]*b[i+size of matrix])
                 return p

MULTIPLY BY INTEGER(x,p)
//Takes an integer "x" and multiplies by a matrix "p"
    for i in p#n
        x*p[i]#n

FORMULA
    #A=B*C-2*(B+C)
    D=MATRIX MULTIPLICATION(B,C)
    E=MATRIX ADDITION(B,C)
    F=MULTIPLY BY INTEGER(2,E)
    A=D-FE
