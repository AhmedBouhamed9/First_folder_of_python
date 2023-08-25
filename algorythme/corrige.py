list1=[5,2,17,15]
n=len(list1)
def list_of_numbers(list):
    for i in range(n):
        for j in range(n-1):
            if list1[j]>list1[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
numbers=list_of_numbers(list1)
print(numbers)