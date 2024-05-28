import re
n1=input("enter somting....")
sp = re.sub(r"([A-Z])", r" \1", n1)
print(sp)

