# n=4

# def count(n):
#     while n>=1:
#         n -=1
#         print(n)
# count(n)
#
def count(a):
    if a<=0:
            return #exit function
    print(a)
    return count(a-1)
n=int(input("give me the number\n"))
result=count(n)
print(result)
 
    
   
    