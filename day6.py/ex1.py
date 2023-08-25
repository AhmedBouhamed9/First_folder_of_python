
files= open (r"C:\Users\Ahmed\OneDrive\Bureau\python\day6.py\ff.txt",'w')
# for i in range(4):
#     names =input ("give me noun")
#     files.write(names+"\n")
    
# files.close()
# ####
name =[]
for i in range(4):
    names =input ("give me noun")
    name.append(names+"\n")
files.writelines(name)