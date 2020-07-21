Python 3.7.3 (default, Oct  7 2019, 12:56:13) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> solution = 'cat'
>>> solution == 'cat'
True
>>> solution != 'cat'
False
>>> 'abracadabra' < 'ace'
True
>>> 'abrda' > 'ace'
False
>>> 'a' <'A'
False
>>> 'a'>'A'
True
>>> 'a' in 'abradacabra'
True
>>> 'p' in 'abbdqwbdu'
False
>>> 'zoo' in 'ooze'
False
>>> '' in 'pas'
True
>>> len("Hello world!")
12
>>> s = 'Learn to Program'
>>> s[0]
'L'
>>> s[1]
'e'
>>> s[25]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[25]
IndexError: string index out of range
>>> len(s)
16
>>> s[16]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s[16]
IndexError: string index out of range
>>> s[15]
'm'
>>> s[-1]
'm'
>>> s[-2]
'a'
>>> s[0:5]
'Learn'
>>> s[6:8]
'to'
>>> s[9:len(s)]
'Program'
>>> s[9:]
'Program'
>>> s[:8]
'Learn to'
>>> s[:]
'Learn to Program'
>>> s[1:8]
'earn to'
>>> s[1:-8]
'earn to'
>>> s[-15:-8]
'earn to'
>>> s[9:15]
'Progra'
>>> s[6]='d'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[6]='d'
TypeError: 'str' object does not support item assignment
>>> s[9:16]='run'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[9:16]='run'
TypeError: 'str' object does not support item assignment
>>> s[:5]+'ed'+s[5:]
'Learned to Program'
>>> s = s[:5]+'ed'+s[5:]
>>> s
'Learned to Program'
>>> import math
>>> math.sqrt(4.0)
2.0
>>> white_rabbit="I'm late! I'm late! For a very important date!"
>>> white_rabbit.lower()
"i'm late! i'm late! for a very important date!"
>>> white_rabbit
"I'm late! I'm late! For a very important date!"
>>> dir(white_rabbit)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.lower)
Help on method_descriptor:

lower(self, /)
    Return a copy of the string converted to lowercase.

>>> help(str.count)
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> white_rabbit.count('ate')
3
>>> "computer".capitalize()
'Computer'
>>> white_rabbit
"I'm late! I'm late! For a very important date!"
>>> white_rabbit.find('late')
4
>>> white_rabbit.find('late', 7)
14
>>> white_rabbit.find('moogah')
-1
>>> white_rabbit.rfind('late')
14
>>> s="        I'm feeling spaced out.          "
>>> s.lstrip()
"I'm feeling spaced out.          "
>>> s.rstrip()
"        I'm feeling spaced out."
>>> s.strip()
"I'm feeling spaced out."
>>> 
