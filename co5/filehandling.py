fn= open("new.txt",'r')
s= fn.read()
print(s)
fn.close()
fn= open("new.txt",'a')
fn.write("changed2\n")
fn.close()
fn= open("new.txt",'r')
s= fn.read()
print(s)
fn.close()
"""
fn= open("new.txt",'w')
fn.write("Testing1.\n")
fn.close()s
#fileobj attributes....
print(fn.closed)
print(fn.name)
print(fn.mode)
"""