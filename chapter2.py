celcius=int(input("enter a number here:"))
fahrenheit=(9/5)*celcius+32
print(celcius,"Celcius","is",fahrenheit,"Fahrenheit")
radius=int(input("enter input here:"))
length=int((input("enter input here:")))
area= radius*radius*3.14
print(area)
volume=area*length
print(volume)
foot=int(input("enter number here:"))
meter=foot*0.305
print(meter)
pounds=int(input("enter a number here:"))
kilograms=pounds*0.454
print(kilograms)
totalcost=int(input("enter number here:"))
tip=int(input("enter what percent tip you want:"))
tip=tip*0.01
totalcost=totalcost+tip*totalcost
print(totalcost)
number=int(input("enter a number here between 1 and 1000:"))
number1=number//10
number4=number1%10
number5=number%10
number6=number//100
number3=number6+number4+number5
print(number3)
minutes=int(input("enter number of minutes here:"))
days=minutes//1440
years=days//365
if days>=365:
	days=days-365*years
	print(years,"years","and",days,"days")
else:
	print(years,"years","and",days,"days")
m=int(input("enter mass of water"))
starttemp=int(input("enter temp of water"))
finaltemp=int(input("enter temp of water"))
q=m*(finaltemp-starttemp)*4184
print(q)
