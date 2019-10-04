x=1
a=[]
b=[]
c=[]
n=0
while x!=0:
	x=float(input("Enter a number here if it is zero the code will end:"))
	a.append(x)
for i in range(0,len(a)):
	if a[i]>0:
		b.append(a[i])
	elif a[i]<0:
		c.append(a[i])
	else:
		break
d=b+c
e=len(b)
f=len(c)
g=len(a)
l=len(d)
h=sum(d)
j=h/l
print(e)
print(f)
print(g)
print(j)
