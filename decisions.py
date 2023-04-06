import random

number = random.randint(0,10)

print(number)

thresh = 5 # short for threshold

if(number > thresh):
    print("Big number")
elif(number < thresh): # else if
    print("Small number")
else: # elif(number == thresh):
    print("Number is", str(thresh))