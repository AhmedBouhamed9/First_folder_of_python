#1-open file
names_file = open(r'C:\Users\Ahmed\OneDrive\Bureau\python\day6.py\name.txt','w')
#2- write file content
names=["Ahmed\n","Bouhamed\n","Monji"]
names_file.writelines(names)

names_file.close()
