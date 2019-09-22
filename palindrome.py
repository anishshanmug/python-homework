# check if a string is a palindrome 
x = "lol"
w = "" 
for i in x: 
    w = i + w 
    if (x==w): 
        print("YES")
    else:
    	print("no")
    