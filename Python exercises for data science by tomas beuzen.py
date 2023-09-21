#Python exercises for data science by tomas beuzen
##Exercise 1 Basics

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


---------------------------------------------------------------------------------------------------------------------------------------------------

#Exercise 2 Loops and functions

"""1. Create a function website() that grabs the website domain from a url string."""

def website(url):
    """Function grabs the website domain from url"""
    domain= url.split('.')[1]
    return domain

my_web= website('www.google.com')
my_web

"""2. Create a function divisible(a, b) that accepts two integers (a and b) and returns True if a is divisble by b without a remainder."""
def divisible(a, b):
    return (a%b== 0)

null= divisible(6,3)
null

"""3. Use list comprehension to square every number in the following list of numbers."""
l= [1,2,3,4,5,6,7,8,9]

for i in l:
    print(i**2)

"""4. For the following list of names, write a list comprehension that creates a list of only words that start with a capital letter."""
names= ['Steve Irwin', 'koala', 'kangaroo', 'Australia', 'Sydney', 'desert']

for name in names:
    for i in name:
        if i.isupper():
            print(name)














def sum_and_product(x,y):
    return(x+y, x*y)
sum_and_product(5,6)

s,_= sum_and_product(5,6)
s
_

names= ['milad', 'tom', 'tiffany']
name= 'tom'
name[::-1]

names_backwards= list()

names_backwards.append(names[0]+names[0][::-1])
names_backwards.append(names[1]+names[1][::-1])
names_backwards.append(names[2]+names[2][::-1])

names_backwards

names_backwards= list()

for name in names:
    names_backwards.append(name+ name[::-1])

names_backwards

def make_palindrome (names):
    names_backwards= list()
    for name in names:
        names_backwards.append(name + name[::-1])
    
    return names_backwards


names1= ['apples', 'oranges', 'bananas']

make_palindrome(names1)

def gen():
    for n in range(10):
        yield(n, n**2)

g=gen()
print(next(g))


x= ([1,2,3], 5)
x[0][1]= 4
x

