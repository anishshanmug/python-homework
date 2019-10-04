import time
currenttime=time.time()
totalseconds=int(currenttime)
currentsecond=totalseconds%60
totalminutes=totalseconds//60
currentminute=totalminutes%60
totalhours=totalminutes//60
currenthour=totalhours%12
l=int(input("Enter number hours offset the time is:"))
currenthour=currenthour+l
print("The current time is",currenthour,":",currentminute,":",currentsecond)