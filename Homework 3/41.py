import math
a=int(input("Enter a number here:"))
b=int(input("Enter a number here:"))
c=int(input("Enter a number here:"))
if math.sqrt(b**2-4*a*c)==0:
	print(-b/(2*a))
elif math.sqrt(b**2-4*a*c)>=0:
	print((-b+math.sqrt(b**2-4*a*c))/2*a)
	print((-b-math.sqrt(b**2-4*a*c))/2*a)
else:
	print("No real solution")