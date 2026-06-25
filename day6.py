>>> #Tuple
>>> empty_tuple = tuple()
>>> tpl = ('item1', 'item2', 'item3')
>>> fruits = ('apple', 'banana', 'orange', 'mango')
>>> len(tpl)
3
>>> len(fruits)
4
>>> first_item = tpl[0]
>>> print(first_item)
item1
>>> second_item = tpl[2]
>>> print(second_item)
item3
>>> first_fruit = fruits[0]
>>> print(first_fruit)
apple
>>> last_index = len(fruits)-1
>>> print(last_index)
3
>>> last_fruit = fruits[last_index]
>>> print(last_fruit)
mango
>>> #Slicing Tuples
>>> tpl = ('item1', 'item2', 'item3', 'item4')
>>> all_items = tpl[0:4]
>>> print(all_items)
('item1', 'item2', 'item3', 'item4')
>>> all_items = tpl[0:]
>>> print(all_items)
('item1', 'item2', 'item3', 'item4')
>>> two_items = tpl[1:3]
>>> print(two_items)
('item2', 'item3')
>>> #Changing Tuples to Lists (if we want to modify a tuple, we should \
change it to a list)
>>> fruits = ('banana', 'orange', 'apple', 'lemon')
>>> fruits = list(fruits)
>>> fruits[0] = 'mango'
>>> print(fruits)
['mango', 'orange', 'apple', 'lemon']
>>> fruits = tuple(fruits)
>>> print(fruits)
('mango', 'orange', 'apple', 'lemon')
>>> #Checking a data in tuple
>>> tpl = ('item1', 'item2', 'item3', 'item4')
>>> 'item2' in tpl
True
>>> 'item5' in tpl
False
>>> print('item1' in tpl)
True
>>> print('item6' in tpl)
False
>>> tpl[0] = 'item6'
Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    tpl[0] = 'item6'
    ~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> #Joining Tuples
>>> tpl1 = ('item1', 'item2', 'item3')
>>> tpl2 = ('item4', 'item5', 'item6')
>>> tpl3 = tpl1+tpl2
>>> print(tpl3)
('item1', 'item2', 'item3', 'item4', 'item5', 'item6')
>>> #Deleting a Tuples
>>> tpl1 = ('item1', 'item2', 'item3')
>>> del tpl1
>>> print(tpl1)
Traceback (most recent call last):
  File "<python-input-46>", line 1, in <module>
    print(tpl1)
          ^^^^
NameError: name 'tpl1' is not defined. Did you mean: 'tpl'?