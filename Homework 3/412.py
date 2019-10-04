x=int(input("Enter a integer here:"))
if x%5==x%6==0:
	print("Is",x,"divisible by 5 and 6?","True")
else:
	print("Is",x,"divisible by 5 and 6?","False")


if x%5==0:
	print("Is",x,"divisible by 5 or 6?","True")	
elif x%6==0:
	print("Is",x,"divisible by 5 or 6?","True")
else:
	print("Is",x,"divisible by 5 and 6?","False")


if x%5==0:
	if x%5==x%6==0:
		pass
		print("Is",x,"divisible by 5 or 6, but not both?","False")
	else:
		print("Is",x,"divisible by 5 or 6, but not both?","True")
elif x%6==0:
	if x%5==x%6==0:
		print("Is",x,"divisible by 5 or 6, but not both?","False")
	else:
		print("Is",x,"divisible by 5 or 6, but not both?","True")
else:
	print("Is",x,"divisible by 5 or 6, but not both?","False")