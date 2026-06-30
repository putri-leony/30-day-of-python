>>> #Conditionals
>>> #If condition
>>> a = 3
>>> if a>0:
...     print('A is a positive number')
...
A is a positive number
>>> #If else
>>> a = 3
>>> if a<0:
...     print('A is a negative number')
... else:
...     print('A is a positive number')
...
A is a positive number
>>> #If elif else
>>> a = 0
>>> if a>0:
...     print('A is a positive number')
... elif a<0:
...     print('A is a negative number')
... else:
...     print('A is zero')
...
A is zero
>>> #Short hand
>>> a = 3
>>> print('A is positive') if a>0 else print('A is negative')
A is positive
>>> a = -2
>>> print('A is negative') if a<0 else print('A is positive')
A is negative
>>> #Nested conditions
>>> a = 0
>>> if a>0:
...     if a%2 == 0:
...         print('A is a positive and even integer')
...     else:
...         print('A is a positive number')
... elif a == 0:
...     print('A is zero')
... else:
...     print('A is a negative number')
...
A is zero
>>> a = 4
>>> if a>0:
...     if a%2 == 0:
...         print('A is a positive and even integer')
...     else:
...         print('A is a positive number')
... elif a == 0:
...     print('A is zero')
... else:
...     print('A is a negative number')
...
A is a positive and even integer
>>> #If condition and logical operators
>>> a = 0
>>> if a>0 and a%2 == 0:
...     print('A is an even and positive integer')
... elif a>0 and a%2 !=0:
...     print('A is a positive integer')
... elif a == 0:
...     print('A is zero')
... else:
...     print('A is negative')
...
A is zero
>>> #If and or logical operators
>>> user = 'putri.leony'
>>> access_level = 3
>>> if user == 'admin' or access_level >=4:
...     print('Access granted!')
... else:
...     print('Access denied')
...
Access denied