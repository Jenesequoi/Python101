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

count= 200
while count!= 100:
    evens= count%2== 0
    count-=1
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


























