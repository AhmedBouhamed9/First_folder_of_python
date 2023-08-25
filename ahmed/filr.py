with open(r"ahmed\file.txt",'w') as write_file:
    names=["ali\n","mongi\n","hachem"]
    write_file.writelines(names)



with open(r"ahmed\file.txt",'r') as read_file:
    content= read_file.read()
    print(content)


with open(r"ahmed\file.txt",'a') as append_file:
    append_file.write("\namado")


with open(r"ahmed\file.txt",'r') as read_file:
    first_line= read_file.readline()#get the first one
    print(first_line)


with open(r"ahmed\file.txt",'r') as read_file:
    content= read_file.readlines()#get all lines in list
    print(content)
    for position,line in enumerate(content):
        print("the position",position,"is",line)
