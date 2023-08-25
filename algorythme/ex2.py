# def sum(n):

#     s=0
#     for i in range (1,n+1):
#         s += i
#     return s
# f=int(input("bhh"))
# result= sum(f)
# print(result)
def sum(b):
    if b==1:
        return 1
    return b+sum(b-1) 
n=int(input(""))
result=sum(n)
print(result)

print(result)
