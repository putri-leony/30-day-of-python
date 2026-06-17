#Variables in Python
first_name = 'Putri'
last_name = 'Leony'
age = 333
person_info = {'first_name':'Putri','last_name':'Leony','age':333}
#printing the values
print('First name:', first_name)
First name: Putri
print('First name length:',len(first_name))
First name length: 5
print('Last name:', last_name)
Last name: Leony
print('Last name length:',len(last_name))
Last name length: 5
print('Age:', age)
Age: 333
first_name, last_name, age = 'Putri', 'Leony', 333
print(first_name, last_name, age)
Putri Leony 333
first_name = input('What is your name:')
What is your name:Putri
age = input('How old are you?')
How old are you?333
age = input('How old are you?')
How old are you?222
print(type('Putri'))
<class 'str'>
print(type(first_name))
<class 'str'>
print(type(True))
<class 'bool'>
print(type(zip([1,2],[3,4])))
<class 'zip'>
#trying to understand zip data type
variables = ['Putri','Leony']
scores = [90,92]
result = zip(variables, scores)
print(type(result))
<class 'zip'>
print(result)
<zip object at 0x0000020EC594E8C0>
#converting one data type to another data type
#int to float
num_int = 10
print('num_int',num_int)
num_int 10
num_float = float(num_int)
print('num_float:',num_float)
num_float: 10.0
#float to int
gravity = 9.81
print(int(gravity))
9
#int to str
num_int = 10
print(num_int)
10
num_str = str(num_int)
print(num_str)
10
#str to int or float
num_str = '10.8'
num_float = float(num_str)
num_int = int(num_float)
print('num_float:',float(num_str))
num_float: 10.8
print('num_int:',int(num_float))
num_int: 10
#str to list
first_name = 'Putri'
print(first_name)
Putri
first_name_to_list = list(first_name)
print(first_name_to_list)
['P', 'u', 't', 'r', 'i']