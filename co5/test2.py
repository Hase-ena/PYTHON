fn = open("new.txt",'r')
s=fn.readlines()

for i in range(0,len(s)):
    print(s[i])
fn.close()
               
