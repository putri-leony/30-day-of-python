>>> #Loops
>>> #While Loop
>>> count = 0
>>> while count < 5:
...     print(count)
...     count = count + 1
...
0
1
2
3
4
>>> count = 3
>>> while count < 5:
...     print(count)
...     count = count + 0.5
...
3
3.5
4.0
4.5
>>> count = 0
>>> while count < 5:
...     print(count)
...     count = count + 1
... else:
...     print(count)
...
0
1
2
3
4
5
>>> count = 3
>>> while count < 5:
...     print(count)
...     count = count + 1
... else:
...     print(count)
...
3
4
5
>>> #Break and Continue
>>> count = 0
>>> while count < 5:
...     print(count)
...     count = count+1
...     if count == 3:
...         break
...
0
1
2
>>> count = 0
>>> while count < 5:
...     if count == 3:
...         count += 1
...         continue
...     print(count)
...     count = count+1
...
0
1
2
4
>>> count = 1
>>> while count < 7:
...     if count == 5:
...         count += 2
...         continue
...     print(count)
...     count = count+1
...
1
2
3
4
>>> count = 11
>>> while count < 20:
...     if count == 3:
...         count += 1
...         continue
...     print(count)
...     count = count+2
...
11
13
15
17
19
>>> count = 5
>>> while count < 20:
...     if count == 7:
...         count += 2
...         continue
...     print(count)
...     count = count+2
...
5
9
11
13
15
17
19
>>> #For Loop
>>> numbers = [0,1,2,3,4,5]
>>> for number in numbers:
...     print(number)
...
0
1
2
3
4
5
>>> language = 'English'
>>> for letter in language:
...     print(letter)
...
E
n
g
l
i
s
h
>>> for i in range(len(language)):
...     print(language[i])
...
E
n
g
l
i
s
h
>>> for i in range(len(language)):
...     print(language[2])
...
g
g
g
g
g
g
g
>>> for i in range(len(language)-3):
...     print(language[2])
...
g
g
g
g
>>> numbers = (0,1,2,3,4,5)
>>> for number in numbers:
...     print(number)
...
0
1
2
3
4
5
>>> score = {'A':76, 'B':54, 'C':89, 'D':92, 'E':68}
>>> for key in score:
...     print(key)
...
A
B
C
D
E
>>> for key, value in score.items():
...     print(key, value)
...
A 76
B 54
C 89
D 92
E 68
>>> it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'Amazon'}
>>> for company in it_companies:
...     print(company)
...
Amazon
Google
Microsoft
Facebook
Apple
>>> numbers = (0,1,2,3,4,5)
>>> for number in numbers:
...     print(number)
...     if number == 3:
...         break
...
0
1
2
3
>>> numbers = (0,1,2,3,4,5)
>>> for number in numbers:
...     print(number)
...     if number == 3:
...         continue
...     print('Next number should be', number+1) if number !=5 else print\
("loop's end")
... print('outside the loop')
...
0
Next number should be 1
1
Next number should be 2
2
Next number should be 3
3
4
Next number should be 5
5
loop's end
outside the loop
>>> numbers = (0,1,2,3,4,5)
>>> for number in numbers:
...     if number >= 5:
...         print("loop's end")
... print('outside the loop')
...
loop's end
outside the loop
>>> numbers = (0,1,2,3,4,5)
>>> for number in numbers:
...     print(number)
...     if number >= 5:
...         print("loop's end")
... print('outside the loop')
...
0
1
2
3
4
5
loop's end
outside the loop
>>> #Range Function
>>> lst = list(range(11))
>>> print(lst)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> st = set(range(1,11))
>>> print(st)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> lst = list(range(0,11,2))
>>> print(lst)
[0, 2, 4, 6, 8, 10]
>>> lst = list(range(0,20,5))
>>> print(lst)
[0, 5, 10, 15]
>>> st = set(range(0,11,2))
>>> print(st)
{0, 2, 4, 6, 8, 10}
>>> lst = list(range(11,0,-2))
>>> print(lst)
[11, 9, 7, 5, 3, 1]
>>> for number in range(11):
...     print(number)
...
0
1
2
3
4
5
6
7
8
9
10
>>> for number in range(0,11,2):
...     print(number)
...
0
2
4
6
8
10
>>> #Nested for Loop
>>> food = {'egg':'fried egg', 'milk':'yoghurt', 'peanut':'peanut butter'\
, 'banana':'banana pancake'}
>>> for key in food:
...     if key == 'milk':
...         for yoghurt in food['milk']:
...             print(yoghurt)
...
y
o
g
h
u
r
t
>>> food = {'egg':'fried egg', 'milk':'yoghurt', 'peanut':'peanut butter'\
, 'banana':'banana pancake'}
>>> for key in food:
...     if key == 'milk':
...         for peanut_butter in food['peanut']:
...             print(peanut_butter)
...
p
e
a
n
u
t

b
u
t
t
e
r
>>> food = {'egg':'fried egg', 'milk':'yoghurt', 'peanut':'peanut butter'\
, 'banana':'banana pancake'}
>>> for key in food:
...     if key == 'yoghurt':
...         for yoghurt in food['milk']:
...             print(yoghurt)
...
>>> #For Else
>>> for number in range(11):
...     print(number)
... else:
...     print('The loops stops at', number)
...
0
1
2
3
4
5
6
7
8
9
10
The loops stops at 10
>>> for number in range(-10,0,1):
...     print(number)
... else:
...     print('negative number stops at', number)
...
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
negative number stops at -1
>>> #Pass
>>> for number in range(6):
...     pass
>>> for number in range(1,6):
...     if number == 3:
...         pass
...     else:
...         print('Number process:', number)
...
Number process: 1
Number process: 2
Number process: 4
Number process: 5