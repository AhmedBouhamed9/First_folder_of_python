def is_palindrome (a):
    n=len(a)
    is_palindromee= True
    for i in range(n//2):
        if a[i]!= a[n-i-1]:       
            is_palindromee= False
    if is_palindromee==True:
        print(a,"is palendrome")
    else:
        print("is not palindrome")
noun=  input("enter a name : ")

is_palindrome(noun)
###########
# a=input ("give me a noun: ")
# i=a[::-1]
# if i==a:
#     print("is_palendrom")
# else:
#     print("is_not_palindrom")