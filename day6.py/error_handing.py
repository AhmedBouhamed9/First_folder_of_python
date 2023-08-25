try:    
    names=["ahmed","mariem","ali"]
    print (names[3])
except IndexError:
    print("there is no index of 2")
print ("end_of the program")
try:
    x = float(input("give me a number\n "))
    y= float(input("give me another one \n"))
    print(x/y)
except ZeroDivisionError:
    print("can't devide by zero")
except ValueError:
    print("X or y should be a number")
    
else:
    print ("works only if thereis no error")
finally:
    print("works aslways")

   