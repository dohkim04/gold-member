import random

numbers = list(range(0,5))

print(numbers)

for number in numbers: # iterate over list
    print(number*2)
    
for i in range(5): # do something fixed number of times
    print("This is from a for loop", str(i))
    
number = random.randint(0, 100)

counter = 0
while number != 52: # do until condition is false
    number = random.randint(0, 100)
    counter += 1
    
print(counter, number)

# deep end

# doing while loop stuff with for loop (bad)
for i in range(1000):
    number = random.randint(0, 100)
    if(number == 52):
        break
    
print(i, number)

# doing for loop stuff with while loop (bad)
i = 0
while i < 5:
    print("This is from a while loop", str(i))
    i += 1


i = 0
while i < len(numbers):
    print(numbers[i]*2)
    i += 1