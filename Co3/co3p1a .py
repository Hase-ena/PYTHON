import random
mylist =['Ann','Ben','alinah','haseena','beli']
print(random.choice(mylist))
print(random.choices(mylist,k=3))
print(random.sample(mylist,k=1))
random.shuffle(mylist)
print(mylist)
print(random.randrange(1111,9999))

