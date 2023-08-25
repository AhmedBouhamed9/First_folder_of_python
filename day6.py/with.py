#without close
try:

    with open("ff.txt",'r') as name_file:
        content=name_file.read()
        print(content)
except (FileNotFoundError, SyntaxError):
    print("file doesn't exist" or " please add an 'r' before the paths")

    #need to close
name_file1= open(r"day6.py/ff.txt",'r')
content1=name_file1.read()
print(content1)
name_file1.close()