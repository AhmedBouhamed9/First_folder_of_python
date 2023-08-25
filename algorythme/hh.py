list1=[17,5,4,23,2,8,30,1,6]
n= len(list1)
list2=[]
for i in range(0,n):
    
    for j in range(i+1,n):

        
        if (list1[i]>list1[j]):
            list2.append(list1[j])
        else:
            list2.append(list1[i])
print(list2)

