import random
a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
print(a)
print(b)
print(c)
d=int(input("Enter the sum of these numbers here:"))
e=a+b+c
if d==e:
	print("You are correct")
else:
	print("That is incorrect,the correct answer was",e)