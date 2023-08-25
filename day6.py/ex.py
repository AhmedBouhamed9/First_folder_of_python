names_file = open(r'C:\Users\Ahmed\OneDrive\Bureau\python\day6.py\names.txt','r')
lines= names_file.readlines()
list =[]
for i in lines:
    a=""
    for j in range (len(i)):
        if i != "\n":
            a= a+i[j]
        list.append(a)
    print (list)
