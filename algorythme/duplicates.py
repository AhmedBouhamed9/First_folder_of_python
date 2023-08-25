a=[1,1,3,1,4,5,8,9,2,2,5,7]

def duplicates(list,element):
    b=[]
    n=len(list)
    for i in range (n):
        if list[i] == element:
            b.append(element)
            
    print(len(b))
        # else:
        #     print("there isn't")
duplicates(a,9)

###
def count_duplicates(array,item):
    count=0
    for number in array:
        if number==item:
            count +=1
    print("has been found",count)
array=[1,1,3,1,4,5,8,9,2,2,5,7]
count_duplicates(array,1)