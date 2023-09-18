#Funtrench Python Exercise
"""1. Print the longest name using counter controlled repetition"""
list= ['Magdalene', 'Joseph', 'Diana', 'Maxim', 'Consolata', 'Kevin', 'Michael']

#set counter
counter= 0

#initiate counter controlled loop
for i in list:
    #find length of string 
    length = len(i)
    if length > counter:
        counter= length
        #print longest name
        print('The longest name is:', i)
    elif length == counter:
        #print longest name
        print('The longest name is: ', i)

"""2. Write a sentinel controlled loop that requests user for integer and stop to exit then prints sum of integers."""
#set variables
count = 0
total = 0
#initiate loop
while True:
   input_value = input('enter number\n')
    #enter sentinel
   if input_value == "Stop":
      break
   try: #force input into integer and tally
      input_value = int(input_value)
      count = count+1
      total = total+input_value
   except: #handle error
      print('invalid data')
       #print sum
      print("The sum is:" , total)







    


    
