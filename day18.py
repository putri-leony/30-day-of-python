>>> #Regular Expressions
>>> import re
#Match
>>> txt = 'I like to watch movies and read some books'
>>> match = re.match('I like to watch movies', txt, re.I)
>>> print(match)
<re.Match object; span=(0, 22), match='I like to watch movies'>
>>> span = match.span()
>>> print(span)
(0, 22)
>>> start, end = span
>>> print(start, end)
0 22
>>> substring = txt[start:end]
>>> print(substring)
I like to watch movies
#Search
>>> txt = 'I like to watch movies and read some books'
>>> match = re.search('movies', txt, re.I)
>>> print(match)
<re.Match object; span=(16, 22), match='movies'>
>>> span = match.span()
>>> print(span)
(16, 22)
>>> start, end = span
>>> print(start, end)
16 22
>>> substring = txt[start:end]
>>> print(substring)
movies
#Difference between match and search
>>> txt = 'I like to watch movies and read some books'
>>> match = re.search('movies', txt, re.I)
>>> print(match)
<re.Match object; span=(16, 22), match='movies'>
>>> match = re.match('movies', txt, re.I)
>>> print(match)
None
>>> #Findall
>>> txt = 'I like to watch movies and read some books'
>>> matches = re.findall('movies', txt, re.I)
>>> print(matches)
['movies']
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> matches = re.findall('horror|Horror', txt)
>>> print(matches)
['horror', 'Horror']
>>> matches = re.findall('[Hh]orror', txt)
>>> print(matches)
['horror', 'Horror']
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> match_replaced = re.sub('horror|Horror', 'romance', txt, re.I)
<python-input-41>:1: DeprecationWarning: 'count' is passed as positional argument
>>> print(match_replaced)
I like to watch romance movies. romance movies excite me
>>> txt = 'Tr%y t%o r%e%ad thi%s. Th%is is j%%ust an %%ex%amp%le'
>>> matches = re.sub('%', '', txt)
>>> print(matches)
Try to read this. This is just an example
#Splitting text
>>> txt = '''This is sentence 1.
... This is sentence 2.
... This is sentence 3.'''
>>> print(re.split('\n', txt))
['This is sentence 1.', 'This is sentence 2.', 'This is sentence 3.']
#Writing RegEx Patterns
>> regex_pattern = r'horror'
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['horror']
>>> matches = re.findall(regex_pattern, txt, re.I)
>>> print(matches)
['horror', 'Horror']
>>> regex_pattern = r'[hH]orror'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['horror', 'Horror']
>> regex_pattern = r'\d'
>>> txt = 'Today is July 14, 2026, and tomorrow is July 15, 2026'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['1', '4', '2', '0', '2', '6', '1', '5', '2', '0', '2', '6']
>>> regex_pattern = r'\d+'
>>> txt = 'Today is July 14, 2026, and tomorrow is July 15, 2026'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['14', '2026', '15', '2026']
>>> regex_pattern = r'[a].'
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['at']
>>> regex_pattern = r'[i].'
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['ik', 'ie', 'ie', 'it']
>>> regex_pattern = r'[i].+'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['ike to watch horror movies. Horror movies excite me']
>>> regex_pattern = r'[l].*'
>>> txt = 'I like to watch horror movies. Horror movies excite me'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['like to watch horror movies. Horror movies excite me']
>>> txt = 'Is it email or e-mail?'
>>> regex_pattern = r'[Ee]-?mail'
>>> matches = re.findall(regex_pattern, txt)
>>> print(matches)
['email', 'e-mail']
>>> number = '6,2016,9,2009'
>>> regex_pattern = r'\d{4}'
>>> matches = re.findall(regex_pattern, number)
>>> print(matches)
['2016', '2009']
>>> regex_pattern = r'\d{1,4}'
>>> print(re.findall(regex_pattern, number))
['6', '2016', '9', '2009']
>>> txt = 'Today is July 14, 2026, and tomorrow is July 15, 2026'
>>> regex_pattern = r'[^A-Za-z]+'
>>> print(re.findall(regex_pattern, txt))
[' ', ' ', ' 14, 2026, ', ' ', ' ', ' ', ' 15, 2026']
#Difference between + and *
>>> txt = 'fruits are banana and apple'
>>> print(re.findall(r'apple.*', txt))
['apple']
>>> print(re.findall(r'apple.+', txt))
[]