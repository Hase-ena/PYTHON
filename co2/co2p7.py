st=input("enter a string:")
s="ing"
for i in range(0,len(st)):
    if st[-3]=='i' and st[-2]=='n' and st[-1]=='g':
        print(st+"ly")
        break
    else:
        print(st+"ing")
        break
'''2nd method'''
str=input("enter a string:")
if str.endswith('ing'):
    str+='ly'
elif len(str)>=3:
    str+='ing'
print(str)