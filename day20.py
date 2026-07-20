>>> #Python PIP
#we have to install pip first, then we can install the packages using pip such as numpy, pandas, requests, etc.
>>> import numpy
>>> numpy.version.version
'2.5.1'
>>> lst = [1,2,3,4,5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr*2
array([ 2,  4,  6,  8, 10])
>>> np_arr+2
array([3, 4, 5, 6, 7])
>>> import pandas
>>> import webbrowser
>>> url_lists = ['https://www.python.org', 'https://github.com/putri-leony']
>>> for url in url_lists:
...     webbrowser.open_new_tab(url)
...
True
True    #immediately opens the links in the browser
>>> #Reading from URL
>>> import requests
>>> url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' #example from Asabeneh
>>> response = requests.get(url)
>>> print(response)
<Response [404]>
>>>
>>> print(response.status_code)
404
>>> print(response.headers)
#give the headers of the response
>>> print(response.text)
#give the content of the response
#Exercise 1
>>> import requests
>>> from collections import Counter
>>> url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
>>> text = requests.get(url).text
>>> words = text.lower().split()
>>> result = Counter(words).most_common(10)
>>> print(result)
[('the', 885), ('and', 776), ('to', 636), ('i', 576), ('a', 541), ('of', 527), ('my', 376), ('in', 375), ('is', 358), ('that', 350)]
>>> #Exercise 2
>>> import requests
>>> import statistics
>>> from collections import Counter
>>> url = 'https://api.thecatapi.com/v1/breeds'
>>> data = requests.get(url).json()
>>> def result(range):
...     number = [float(x) for x in range.split('-')]
...     return statistics.mean(number)
...
>>> weight = [result(cat['weight']['metric']) for cat in data]
>>> age = [result(cat['life_span']) for cat in data]
>>> print(f"""
... ===Statistics of Cat Weight===
... min   : {min(weight)}
... max   : {max(weight)}
... mean  : {statistics.mean(weight):.2f}
... median: {statistics.median(weight)}
... std   : {statistics.stdev(weight):.2f}
... """)

===Statistics of Cat Weight===
min   : 3.0
max   : 7.5
mean  : 4.71
median: 4.5
std   : 1.07
>>> print(f"""
... ===Statistics of Cat Age===
... min   : {min(age)}
... max   : {max(age)}
... mean  : {statistics.mean(age):.2f}
... median: {statistics.median(age)}
... std   : {statistics.stdev(age):.2f}
... """)

===Statistics of Cat Age===
min   : 10.5
max   : 19.0
mean  : 13.75
median: 13.5
std   : 1.58