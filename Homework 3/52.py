import random
import time

correctCount=0
count=0
Number_Of_Questions=10
starttime=time.time()
while count<Number_Of_Questions:
	number1=random.randint(1,15)
	number2=random.randint(1,15)
	answer=eval(input("What is"+str(number1)+"+"+str(number2)+"?"))
	if number1+number2==answer:
		print("You are correct")
		correctCount+=1
	else:
		print("Your answer is wrong.\n",number1,"+",number2,"is",number1+number2)
	count+=1
endtime=time.time()
testtime=int(endtime-starttime)
print("Correct count is",correctCount,"out of",Number_Of_Questions,"\nTest time is",testtime,"seconds")
