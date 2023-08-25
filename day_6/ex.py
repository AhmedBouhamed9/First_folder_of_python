def tuple(n,b):
    print ("before change" , n ,b)
    temp = n[0]
    n[0]=b[0]
    b[0]= temp
    temp = n[-1]
    n[-1]=b[-1]
    b[-1]= temp
    print (n," and " , b)
n=[1,2,3]
b=[4,5,6]
tuple (n,b)



    