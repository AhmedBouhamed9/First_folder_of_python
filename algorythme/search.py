# list1=[2,1,15,7,8]
# n=len(list1)
# def search(list,a):
#     for index,i in enumerate(list):
#         if i==a:
#             print(i,"has position ",index)

# search(list1)
list1=[2,1,15,7,8]
def search(list,a):
    position= None
    for i in range(len(list)):
        #print(list[i],a)debugging
        if list[i]==a:
            position=i
            break
    if position==None:
        print("not found")
    else:
            print("found with position ",position)
n=int(input ("give me a number to search :  "))
search(list1,n)
######
