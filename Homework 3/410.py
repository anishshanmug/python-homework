import random
import random
a=random.randint(0,100)
b=random.randint(0,100)
print(a)
print(b)
d=int(input("Enter the product of these numbers here:"))
e=a*b
if d==e:
	print("You are correct")
else:
	print("That is incorrect,the correct answer was",e)