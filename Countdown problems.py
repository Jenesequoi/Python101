#countdown problems
"""1. Using a while loop, print numbers from 50 to 0."""

count= 50
while count!= 0:
    count-=1
    print(count)

"""2. Using a while loop, print odd numbers from 100 to 1."""

count= 100
while count!= 0:
    odds= count%2== 0
    count-= 1
    if odds== 1:
        print(count)

"""3. Using a while loop, print even numbers from 200 to 100."""
#Initialise count of 200
count= 200
#introduce loop until count becomes 100
while count!= 100:
    #introduce variable which checks if the remainder of count/2 is 0
    evens= count%2== 0
    #subtract 1 from count while loop is running
    count-=1
    #if the variable evens is true, print count.
    if evens== 0:
        print(count)

"""4. Use a while loop to ask the user for 5 numbers.  Print the average of those numbers."""
count=0 
sum= 0
average= 0
while count <5:
    data= int(input("Enter number: "))
    count+= 1
    sum += data
    average= (sum/count)
    if count== 5:
        print("Average:", average)

"""5. Use a while loop to ask the user for 7 numbers.  Print the maximum number."""
count= 0
maximum= None

while count< 7:
    number= int(input("Enter number: "))
    count+= 1
    if maximum is None or number> maximum:
        maximum= number
    if count== 7:
        print("The maximum number is: ", maximum)

"""6. Use a while loop to ask the user for 6 numbers.  Print the minimum number."""
count= 0
minimum= None

while count<7:
    number= int(input("Enter number: "))
    count+=1
    if minimum is None or number< minimum:
        minimum= number       
    if count== 7:
        print("The minimum number is", minimum)

"""7. You play Roblox and have 5000 Robux.
You want to buy 3 items. In a while loop, ask the user how much each item costs.
Display the amount of Robux you have to start and the amount you have remaining
"""
roblox= 5000
purchase= 0
while purchase<3:
    amount= int(input("How much?"))
    roblox= roblox-amount
    purchase+=1
    if purchase== 3:
        print("Here's your change:", roblox, "Roblox")

"""8. You eat a Chicken Burrito which is 1165 calories and now want to burn off these calories.
You burn 8 calories per minute walking around.
Use a while loop to display a chart to display how many calories you have left to burn off from 60 minutes to 0.
"""
walkminutes= 0
initialcalories= 1165
calories_per_walkminute= 8
while walkminutes!= 60:
    walkminutes+= 1
    caloriesleft= initialcalories- (calories_per_walkminute*walkminutes)
    print(walkminutes, caloriesleft)

"""After your exercise, you get even more hungry and eat a Big Mac which is 540 calories. Add these calories to the amount you have left after walking.
You burn 10 calories per minute running.
Use another while loop to display a chart to display how many calories you have left to burn off from 30 minutes to 0.
"""
caloriesleft= 685
bigmac= 540
calories_per_runminute= 10
runtime= 0
while runtime!= 30:
    runtime+= 1
    runburn= calories_per_runminute*runtime
    currentcalories= (caloriesleft+ bigmac)- runburn
    print("Runtime", runtime, "Runburn", runburn, "Calories", currentcalories)

"""9. Use a while loop to display a table of Celsius temperatures from 20 to 10 and their Fahrenheit equivalents."""

















