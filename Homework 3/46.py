p=int(input("Enter your weight in pounds:"))
h=int(input("Enter the number of feet your height is:"))
h1=int(input("Enter the number of inches your height is:"))
h2=(h*12)+h1
Bmi=(p*705)/(h2*h2)
print(Bmi)