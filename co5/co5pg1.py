fn = open("new.txt",'r')
s=fn.readlines()
l=[line.strip() for line in s]
print(l)
print([line.strip() for line in open("new.txt",'r')])