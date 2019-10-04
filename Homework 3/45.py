Sunday=0
Monday=1
Tuesday=2
Wednesday=3
Thursday=4
Friday=5
Saturday=6
a=[Sunday,"Sunday",Monday,"Monday",Tuesday,"Tuesday",Wednesday,"Wednesday",Thursday,"Thursday",Friday,"Friday",Saturday,"Saturday"]
x=int(input("Enter today's day:"))
y=int(input("Enter The number of days elapsed since today:"))
z=y-x
for i in range(0,len(a)):
	if x==a[i]:
		z=abs(z)
		z=z+1
		print("Today is",a[i+1],"and the future day is",a[z+i+z+1])
