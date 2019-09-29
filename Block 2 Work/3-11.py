num = int(input("Please Enter any Number: "))    
rev = 0    
while(num > 0):    
    mod = num %10    
    rev = (rev *10) + mod    
    num = num //10    
     
print("Reverse of entered number is = %d" %rev)   
