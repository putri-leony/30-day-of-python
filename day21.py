>>> #Classes and Objects
>>> #(create a class to create an object)
>>> #Creating a Class
>>> class Person:
...     pass
... print(Person)
...
<class '__main__.Person'>
>>> #Creating an Object
>>> p = Person()
>>> print(p)
<__main__.Person object at 0x0000019D88F3B230>
>>> #Class Constructor
>>> class Person:
...     def __init__ (self, name):
...         self.name = name
...
>>> p = Person('Putri Leony')
>>> print(p.name)
Putri Leony
>>> print(p)
<__main__.Person object at 0x0000019D88F3B620>
>>> class exam_score:
...     def __init__ (self, name, score):
...         self.name = name
...         self.score = score
...
>>> lists = [exam_score('Linda', 87),exam_score('John',80),exam_score('Lily', 75)]
>>> for student in lists:
...  print(f"Name: {student.name} | Score: {student.score}")
...
Name: Linda | Score: 87
Name: John | Score: 80
Name: Lily | Score: 75
>>> #Object Methods
>>> class Person:
...  def __init__(self, name, city):
...   self.name = name
...   self.city = city
...  def greetings(self):
...   return f'Hello {self.name}, welcome to {self.city}!'
...
>>> p = Person('Jane', 'Wonderland')
>>> print(p.greetings())
Hello Jane, welcome to Wonderland!
>>> class Student:
...     def __init__ (self, name, score):
...      self.name = name
...      self.score = score
...     def info(self):
...      return f'Student: {self.name} | Score: {self.score}'
...
>>> students = [
... Student('Jane', 78),
... Student('John', 87),
... Student('Doe',58)
... ]
>>> for p in students:
...     print(p.info())
...
Student: Jane | Score: 78
Student: John | Score: 87
Student: Doe | Score: 58
>>> #Object Default Methods
>>> class Person:
...     def __init__(self, name='Jane', city='Wonderland'):
...         self.name = name
...         self.city = city
...     def person_info(self):
...         return f'Hello {self.name}, welcome to {self.city}!'
...
>>> p1 = Person()
>>> print(p1.person_info())
Hello Jane, welcome to Wonderland!
>>> p2 = Person('John', 'Wakanda')
>>> print(p2.person_info())
Hello John, welcome to Wakanda!
>>> #Modify Class Default Values
>>> class Person:
...     def __init__(self, name='Jane', city='Wonderland'):
...         self.name = name
...         self.city = city
...         self.skills = []
...     def person_info(self):
...         return f'Hello {self.name}, welcome to {self.city}!'
...     def add_skill(self, skill):
...         self.skills.append(skill)
...
>>> p1 = Person()
>>> print(p1.person_info())
Hello Jane, welcome to Wonderland!
>>> p1.add_skill('Python')
>>> p1.add_skill('HTML')
>>> p1.add_skill('JavaScript')
>>> class Person:
...     def __init__(self, name, score):
...         self.name = name
...         self.score = score
...         self.skills = []
...     def person_info(self):
...         return f'Name: {self.name} | Score: {self.score}'
...     def add_skill(self, skill):
...         self.skills.append(skill)
...
>>> #Inheritance
>>> class student(Person):
...     pass
...
>>> s1 = student('Jane', 85)
>>> s2 = student('John', 78)
>>> print(s1.person_info())
Name: Jane | Score: 85
>>> s1.add_skill('Python')
>>> s1.add_skill('JavaScript')
>>> print(s1.skills)
['Python', 'JavaScript']
>>> print(f"""
... {s1.person_info()}
... skills: {s1.skills}
... """)

Name: Jane | Score: 85
skills: ['Python', 'JavaScript']
>>> s2.add_skill('Writing')
>>> s2.add_skill('Data Analyst')
>>> print(f"""
... {s2.person_info()}
... skills: {s2.skills}
... """)

Name: John | Score: 78
skills: ['Writing', 'Data Analyst']