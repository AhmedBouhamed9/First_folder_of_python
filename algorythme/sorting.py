list1=[7,8,6,4,1,9,6,5,7]
n= len(list1)
for i in range(0,n):
    
    for j in range(i+1,n):

        
        if (list1[i]>list1[j]):
            a=list1[i]
            list1[i]=list1[j]
            list1[j]=a
print(list1)
list1=[17,5,4,23,2,8,30,1,6]
n= len(list1)
list2=[]
for i in range(0,n):
    
    for j in range(i+1,n):

        
        if (list1[i]>list1[j]):
            list2.append(list1[j])
        else:
            list2.append(list1[i])
print(set(list2))
l=[1,5,2,3]
l2=[]
for i in range(len(l)):
    minimum=min(l)
    l.remove(minimum)
    l2.append(minimum)
print(l2)
