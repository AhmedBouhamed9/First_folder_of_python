import pprint
def creat():
    nombre_of_rows=int(input("enter the number of rows"))
    nombre_of_coloumns=int(input("enter the number of colouns"))
    matrix=[]
    for i in range(nombre_of_rows):
        row=[]
        for j in range(nombre_of_coloumns):
            number=int(input("enter number : "))
            row.append(number)
        matrix.append(row)
    pprint.pprint(matrix)
creat()