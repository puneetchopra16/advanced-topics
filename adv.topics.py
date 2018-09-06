from math import *
#question1


li=[1,2,3,4,5]
m=[i**3 for i in li]
print(m)

#question2


list=[x for x in range(2, 20)
     if all(x % y != 0 for y in range(2, x))]
print(list)

#question3


'''
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.

The type of data returned by list comprehensions and generator expressions differs.

The generator yields one item at a time — thus it is more memory efficient than a list.'''


#question4


Celsius = [39.2, 36.5, 37.3, 37.8]
li=list(map(lambda x: (x*1.8)+32,Celsius))
print(li)


#question5


number = [1,2,3,4,5]
li=list(map(lambda x: x**2,number))
print(li)

#question6


import sympy
num=[1,2,3,4,5,6,7,8,9,10,11,12]
li = list(filter(lambda x: True if sympy.isprime(x) else False, num))
print(li)

#question7


from functools import *

li=[1,2,3,4,5]
product = reduce((lambda x, y: x * y), li)
print(product)

