My__Number = int(input("Please provide the number to be mirror: "))
mirror__Number = 0
while(My__Number > 0):
 Reminder = My__Number %10
 mirror__Number = (mirror__Number *10) + Reminder
 My__Number = My__Number //10
print("mirror of the provided number is = %d" %mirror__Number)
