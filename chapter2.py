import math
import time
print(1)
celcius=int(input("enter a number here:"))
fahrenheit=(9/5)*celcius+32
print(celcius,"Celcius","is",fahrenheit,"Fahrenheit")
print(2)
radius=int(input("enter input here:"))
length=int((input("enter input here:")))
area= radius*radius*3.14
print(area)
volume=area*length
print(volume)
print(3)
foot=int(input("enter number here:"))
meter=foot*0.305
print(meter)
print(4)
pounds=int(input("enter a number here:"))
kilograms=pounds*0.454
print(kilograms)
print(5)
totalcost=int(input("enter number here:"))
tip=int(input("enter what percent tip you want:"))
tip=tip*0.01
totalcost=totalcost+tip*totalcost
print(totalcost)
print(6)
number=int(input("enter a number here between 1 and 1000:"))
number1=number//10
number4=number1%10
number5=number%10
number6=number//100
number3=number6+number4+number5
print(number3)
print(7)
minutes=int(input("enter number of minutes here:"))
days=minutes//1440
years=days//365
if days>=365:
	days=days-365*years
	print(years,"years","and",days,"days")
else:
	print(years,"years","and",days,"days")
print(8)
m=int(input("enter mass of water"))
starttemp=int(input("enter temp of water"))
finaltemp=int(input("enter temp of water"))
q=m*(finaltemp-starttemp)*4184
print(q)
print(9)
at=int(input("Enter a number between -58 and 41:"))
ws=int(input("Enter a number above 2:"))
windchill=35*(.74+0.6125*at-35.75*(ws**0.16)+0.4275*at*(ws**0.16))
print(windchill)
print(10)
v=int(input("Enter airplane speed here:"))
a=int(input("Enter airplane acceleration here:"))
length=v**2/2*a
print(length)
print(11)
ir=int(input("What is the monthly interest rate:"))
ida=5000/((1+ir)**36)
print(ida)
print(12)
a=1
b=2
for i in range(0,5):
	print(a,b,a**b)
	a=a+1
	b=b+1
integer=int(input("Enter a four digit number here:"))
integer1=integer%10
integer2=integer//10
integer3=integer2%10
integer4=integer//1000
integer5=integer//100
integer6=integer5%10
print(integer4)
print(integer6)
print(integer3)
print(integer1)
z=[]
for i in range(0,3):
	a=int(input("Enter x coordinate here:"))
	b=int(input("Enter y coordinate here"))
	z.append(a)
	z.append(b)
side1=math.sqrt((z[2]-z[0])**2+(z[3]-z[1])**2)
side2=math.sqrt((z[4]-z[2])**2+(z[5]-z[3])**2)
side3=math.sqrt((z[4]-z[0])**2+(z[5]-z[1])**2)
s=(side1+side2+side3)/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(area)
side=int(input("Enter side length here"))
are1=(3*(math.sqrt(3))*side*side)/2
print(are1)
v=int(input("Enter the starting velocity"))
v1=int(input("Enter the end velocity"))
t=int(input("Enter the amount of time it took"))
a=(v1-v)/t
p=int(input("Enter your weight in pounds:"))
h=int(input("Enter your height in inches:"))
Bmi=(p*705)/(h*h)
print(Bmi)
currenttime=time.time()
totalseconds=int(currenttime)
currentsecond=totalseconds%60
totalminutes=totalseconds//60
currentminute=totalminutes%60
totalhours=totalminutes//60
currenthour=totalhours%24
l=int(input("Enter number hours offset the time is"))
currenthour=currenthour+l
print("The current time is",currenthour,":",currentminute,":",currentsecond)
investmentamount=int(input("Enter a investment amount here:"))
interestrate=int(input("enter the annual interest rate here:"))
years1=int(input("enter the number of years here:"))
value=investmentamount*(1+interestrate)**years1
balance=int(input("enter a value here:"))
intrestrate=int(input("enter a value here:"))
inter=balance*(intrestrate/1200)
savings=int(input("enter a value here:"))
accountbalance=savings*(1+0.00417)
print("After six months you have",accountbalance,"In your account")
years2=int(input("Enter the number of years:"))
births=31536000//7
deaths=31536000//13
immigrants=31536000//45
futurepopulation=(312032486+(births+immigrants-deaths)*years2)
print(futurepopulation)