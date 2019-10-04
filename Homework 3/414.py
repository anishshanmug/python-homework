import random 
coin=['heads','tails'] 
y=random.choice(coin)
x=input("Enter heads or tails:")
if x==y:
	print("It is",y,"!")
else:
	print("Sorry it was",y)