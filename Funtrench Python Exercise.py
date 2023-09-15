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





    
