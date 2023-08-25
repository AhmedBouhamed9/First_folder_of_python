names= open(r"C:\Users\Ahmed\OneDrive\Bureau\python\challenge.py\ch1.txt",'a')
for i in range (3):
    name=input("enter names \n")
    p=name+"\n"
    names.write(p)
names.close()
