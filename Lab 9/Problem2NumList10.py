# Zhyldyz Torogulova
# 11/19/25
# Problem2 - Using a while loop, create a list called L that contains the numbers 0 to 10. On each
# iteration, the loop should append the current value of a counter variable to the list and then
# increase the counter by 1. The while loop should stop once the counter variable is greater than
# 10
l = [] #create list for numbers
i = 0 #to control the loop
while len(l) <= 10:  #while our lists lenght is not 10
    l.append(int(i)) #it will add number (the controler)
    i += 1 #controls loop and at the same time works as number varuable
print(l)
