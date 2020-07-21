Python 3.7.3 (default, Oct  7 2019, 12:56:13) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1
>>> y=x+2
>>> x=7
>>> y
3
>>> x
7
>>> kill x
SyntaxError: invalid syntax
>>> ord(-5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ord(-5)
TypeError: ord() expected string of length 1, but int found
>>> c=6
>>> ord(c)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord(c)
TypeError: ord() expected string of length 1, but int found
>>> ord(1,2,3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord(1,2,3)
TypeError: ord() takes exactly one argument (3 given)
>>> ord(t)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord(t)
NameError: name 't' is not defined
>>> ord(...)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ord(...)
TypeError: ord() expected string of length 1, but ellipsis found
>>> ord(c, /)
SyntaxError: invalid syntax
>>> ord(c, 5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ord(c, 5)
TypeError: ord() takes exactly one argument (2 given)
>>> ord(c, d)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ord(c, d)
NameError: name 'd' is not defined
>>> ord()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ord()
TypeError: ord() takes exactly one argument (0 given)
>>> ord('c')
99
>>> ord("c")
99
>>> ord(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ord(c)
TypeError: ord() expected string of length 1, but int found
>>> ord('c','d')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ord('c','d')
TypeError: ord() takes exactly one argument (2 given)
>>> help(ord)
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

>>> ord(...)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ord(...)
TypeError: ord() expected string of length 1, but ellipsis found
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> round(5)
5
>>> round(5, 2)
5
>>> round()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    round()
TypeError: round() missing required argument 'number' (pos 1)
>>> def f(x)
SyntaxError: invalid syntax
>>> def(x):
	
SyntaxError: invalid syntax
>>> def f(x):
	return x**2

>>> f(9)
81
>>> 
