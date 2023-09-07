year = int(input ("Please enter the year number"))
if (year%400==0):
  print ("%d is a Leap year"%year)
elif(year%100==0):
  print ("%d is Not the leap year"%year)
elif(year%4==0):
  print ("%d is a Leap year"%year)
else:
  print("%d is Not the Leap year"%year)