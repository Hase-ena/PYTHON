fn = open("new.txt",'r')
f2 = open("new1.txt",'w')
s=fn.readlines()

for i in range(0,len(s)):
    if i%2 !=0:
        f2.write(s[i])
fn.close()
f2.close()
f2 = open("new1.txt",'r')
t= f2.read()
print(t)