#1-open file
names_file = open(r'C:\Users\Ahmed\OneDrive\Bureau\python\day6.py\names.txt','r')
#2- read file content
# content= names_file.read()#read all the content kol wa7da fi star
#lines= names_file.readlines()#read all lines
line= names_file.readline()#read only one line
#3-manipulation
# print(content)
list=[]
for n in lines : 
    list.append(
        n.replace("\n","")
    )
print(list)
#print("line\n", line)
#4-close file
names_file.close()
#comment : ctrl + k +c