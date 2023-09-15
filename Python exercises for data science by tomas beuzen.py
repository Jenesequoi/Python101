#Python exercises for data science by tomas beuzen
##Exercise 1

"""1. Arithmetics"""
i= 5**5
i

"""2. Find remainder"""
i= 73%6
i

"""3. Find whole number and remainder""" 
i= 123//3
i
i= 123%3
i

"""4. Split string into a list on the space character"""
s= "MDS is going virtual!"
s.split()

"""5. Use f string to print variables"""
thing= 'light'
speed= 299792458
print (f'The speed of {thing} is {speed}')

"""6. Extract 'MDS' from nested list using indexing"""
l= [10, [3,4], [5,[100,200,["MDS"]], 23,11],1,7]

word= l[2][1][2][0]
word

"""7. Grab 'MDS' from nested dictionary"""
d= {
    'outer':[
        1,
        2,
        3,
        {'inner':['this', 'is', 'inception',{'inner_inner':[1,2,3, 'MDS']}]},
    ]
}
word= d['outer'][3]['inner'][3]['inner_inner'][3]
word

"""8. Explain error"""
t= (1, 2, 3, 4, 5)
t[-1]= 6 #tuples are immutable

"""9. Extract domain from email"""
email= 'tomas.beuzen@fakemail.com'
email.split("@")[-1].split('.com')[0]

"""10. Given the variable language which contains a string, use if/elif/else to write a program that:

return “I love snakes!” if language is "python" (any kind of capitalization)

return “Are you a pirate?” if language is "R" (any kind of capitalization)

else return “What is language?” if language is anything else."""

language = 'python'

if language == 'python':
    print('I love snakes')
elif language == 'R':
    print('Are you a pirate?')
else: print('What is {}. format(language)')











