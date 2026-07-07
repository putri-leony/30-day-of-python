>>> #List Comprehension
>>> language = 'Python'
>>> lst =  list(language)
>>> print(lst)
['P', 'y', 't', 'h', 'o', 'n']
>>> print(type(lst))
<class 'list'>
>>> lst = [i for i in language]
>>> print(type(lst))
<class 'list'>
>>> print(lst)
['P', 'y', 't', 'h', 'o', 'n']
>>> numbers = [i for i in range(11)]
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> squares = [i * i for i in range(11)]
>>> print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> numbers = [(i, i*i) for i in range(11)]
>>> print(numbers)
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
>>> even_numbers = [i for i in range(21) if i%2==0]
>>> print(even_numbers)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> odd_numbers = [i for i in range(21) if i%2 != 0]
>>> print(odd_numbers)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> numbers = [-8,-7,-6,-5,-4,-3,0,1,3,4,5,7,6,8,10]
>>> positive_even_numbers = [i for i in numbers if i%2 == 0 and i>0]
>>> print(positive_even_numbers)
[4, 6, 8, 10]
>>> list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
>>> flattened_list = [number for row in list_of_lists for number in row]
>>> print(flattened_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #Lambda Function
>>> def add_two_nums(a,b):
...     return a+b
...
>>> print(add_two_nums(2,3))
5
>>> add_two_nums = lambda a,b: a+b
>>> print(add_two_nums(2,3))
5
>>> (lambda a,b: a+b)(5,9)
14
>>> square = lambda x: x**2
>>> print(square(3))
9
>>> cube = lambda x: x**3
>>> print(cube(5))
125
>>> multiple_variable = lambda a,b,c: a**2-3*b+4*c
>>> print(multiple_variable(5,5,3))
22
>>> def power(x):
...     return lambda n: x**n
...
>>> cube = power(2)(3)
>>> print(cube)
8
>>> two_power_of_five = power(2)(5)
>>> print(two_power_of_five)
32
>>> numbers = [-4,-3,-2,-1,0,2,4,6]
>>> negative_numbers = [i for i in numbers if i<0 and i == 0]
>>> print(negative_numbers)
[]
>>> negative_numbers = [i for i in numbers if i<0]
>>> print(negative_numbers)
[-4, -3, -2, -1]
>>> zero_only = [i for i in numbers if i == 0]
>>> print(zero_only)
[0]
>>> #Exercise 2
>>> lst = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11\
)]
>>> print(lst)
[(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32), (3, 1, 3, 9, 27, 81, 243), (4, 1, 4, 16, 64, 256, 1024), (5, 1, 5, 25, 125, 625, 3125), (6, 1, 6, 36, 216, 1296, 7776), (7, 1, 7, 49, 343, 2401, 16807), (8, 1, 8, 64, 512, 4096, 32768), (9, 1, 9, 81, 729, 6561, 59049), (10, 1, 10, 100, 1000, 10000, 100000)]
>>> for item in lst:
...     print(item)
...
(0, 1, 0, 0, 0, 0, 0)
(1, 1, 1, 1, 1, 1, 1)
(2, 1, 2, 4, 8, 16, 32)
(3, 1, 3, 9, 27, 81, 243)
(4, 1, 4, 16, 64, 256, 1024)
(5, 1, 5, 25, 125, 625, 3125)
(6, 1, 6, 36, 216, 1296, 7776)
(7, 1, 7, 49, 343, 2401, 16807)
(8, 1, 8, 64, 512, 4096, 32768)
(9, 1, 9, 81, 729, 6561, 59049)
(10, 1, 10, 100, 1000, 10000, 100000)