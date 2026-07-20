f = open('C:/users/sipul/Downloads/example.txt')
>>> print(f)
<_io.TextIOWrapper name='C:/users/sipul/Downloads/example.txt' mode='r' encoding='cp1252'>
>>> txt = f.read()
>>> print(type(txt))
<class 'str'>
>>> print(txt)
example 1 example 2 example 3 example 4 example 5
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> txt = f.read(10)
>>> print(type(txt))
<class 'str'>
>>> print(txt)
example 1
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> txt = f.read(11)
>>> print(txt)
example 1 e
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> txt = f.read()
>>> print(txt)
example 1 example 2 example 3 example 4 example 5
line 1 line 2 line 3 line 4 line 5
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> line = f.readline()
>>> print(line)
example 1 example 2 example 3 example 4 example 5
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> lines = f.readlines()
>>> print(lines)
['example 1 example 2 example 3 example 4 example 5\n', 'line 1 line 2 line 3 line 4 line 5']
>>> f.close()
>>> f = open('C:/users/sipul/Downloads/example.txt')
>>> lines = f.read().splitlines()
>>> print(type(lines))
<class 'list'>
>>> print(lines)
['example 1 example 2 example 3 example 4 example 5', 'line 1 line 2 line 3 line 4 line 5']
>>> with open('C:/users/sipul/Downloads/example.txt') as f:
...     lines = f.read().splitlines()
...     print(type(lines))
...     print(lines)
...
<class 'list'>
['example 1 example 2 example 3 example 4 example 5', 'line 1 line 2 line 3 line 4 line 5']
>>> #Opening Files for Writing/Updating
>>> with open('C:/users/sipul/Downloads/example.txt','a') as f:
...     f.write('I want to add this sentence')
...
27 #if I open the file, the new sentence is added at the end of the file
>>> with open('C:/users/sipul/Downloads/example.txt','w') as f:
...     f.write('How about this sentence')
...
23 #all of my text is replaced with this new sentence
>>> #Deleting Files
>>> import os
>>> os.remove('C:/users/sipul/Downloads/example.txt') #already deleted
>>> if os.path.exists('C:/users/sipul/Downloads/example.txt'):
...     os.remove('C:/users/sipul/Downloads/example.txt')
... else:
...     print('The file does not exist')
...
The file does not exist
#Example of opening a file types
#Excel
>>> import openpyxl
>>> excel_book = openpyxl.load_workbook(r'D:\Peng data modul 1.xlsx') #example of one of my excel files
>>> print(excel_book.sheetnames)
['modul 1', 'Sheet1']
>>> print(len(excel_book.sheetnames))
2
