#Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints 
# “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

import datetime
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    print("Good Morning")
elif currentTime.hour > 12 and currentTime.hour < 18:
    print("Good Afternoon")
elif currentTime.hour > 17 and currentTime.hour < 23:
    print("Good Evening")
elif currentTime.hour > 22:
    print("Good Night")