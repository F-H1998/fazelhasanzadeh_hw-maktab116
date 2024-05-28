n1= input("enter somting pl.....")
space = ""
for i in n1:
    if i.isupper():
        space += " "
    space += i
print(space.strip())
