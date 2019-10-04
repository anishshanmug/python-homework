import random
print("Rock,Paper,Scissors Game")
a=["rock","paper","scissors"]
i=0
j=0
while i<3 and j<3:
	print(i)
	print(j)
	x=input("Please enter rock,paper or scissors: ")
	computer=random.choice(a)
	print(computer)
	if computer==x:
		print("It's a tie")

	elif computer=="scissors" and x=="rock":
		print("You win")
		i=i+1
		
	elif computer=="rock" and x=="scissors":
		print("You lose")
		j=j+1
		
	elif computer=="paper" and x=="rock":
		print("You lose")
		j=j+1
		
	elif computer=="paper" and x=="scissors":
		print("You win")
		i=i+1
		
	elif computer=="rock" and x=="paper":
		print("You win")
		i=i+1
		
	elif computer=="scissors" and x=="paper":
		print("You lose")
		j=j+1
print("Your wins:",i)
print("Computer wins:",j)	