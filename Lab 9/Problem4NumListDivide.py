# Zhyldyz Torogulova
# 11/19/25
# Problem 4: Create a while loop that initializes a counter at 0 and will run until the counter
# reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement
limit = 0   #controller
i = 0 #number varuable
tens = []  #array for numbers dividable 10
while limit <= 50:
    print(i)  #prints numbers until reaches 50
    i += 1
    limit = limit + 1
    if i % 10 == 0: #if dividable to 10
        tens.append(i) #then it goes to our list ten
print(tens)
