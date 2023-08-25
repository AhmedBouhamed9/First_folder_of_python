# import math
# print(math.factorial(5))
# result=1
# i =int(input("donner un nombre"))
# for n in range(1,i+1):
#     result=result*n
# print(result)
# n=int(input("give me a number\n"))
# result=1
# i=1
# while i<=n:

#     result=result*i 
#     i +=1
# print(result)
def factorial(n):
    #base case
    if n==1:
        return 1
    #recursive case
    return n*factorial(n-1)
n= int(input("give me a number\n"))
result=factorial(n)
print(result)
