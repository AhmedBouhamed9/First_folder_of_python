my_list =[1,5,8,8,9,5,6,1,3,2,6,1]
set1 = set (my_list)
print (set1)
leng = int ( len(sorted(set1)))
number = 0
for number in set1:
    print (number, "its frequency is ",my_list.count(number))
    number +=1

