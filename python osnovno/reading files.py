Python 3.7.5 (default, Nov 20 2019, 09:21:52) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> grades = [['Assignement 1', 80], ['Assignement 2', 90], ['Assignment 3', 70]]
>>> len(grades)
3
>>> len(grades[1])
2
>>> grades[1]
['Assignement 2', 90]
>>> len(grades[1][0])
13
>>> for item in grades:
	print(item)

['Assignement 1', 80]
['Assignement 2', 90]
['Assignment 3', 70]
>>> 
= RESTART: /home/karlo/Desktop/pythoni/nested list.py
>>> calculate_average([['A1', 80], ['A2', 90]])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    calculate_average([['A1', 80], ['A2', 90]])
NameError: name 'calculate_average' is not defined
>>> 
= RESTART: /home/karlo/Desktop/pythoni/nested list.py
>>> calculate_average([['A1', 80], ['A2', 90]])
85.0
>>> grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]
>>> english = grades [0]
>>> english
[70, 75, 80]
>>> total = 0
>>> for mark in english:
	total = total + mark

>>> total
225
>>> total / len (english)
75.0
>>> 
= RESTART: /home/karlo/Desktop/pythoni/nested list.py
>>> pas = average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pas = average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
  File "/home/karlo/Desktop/pythoni/nested list.py", line 39, in average
    averages.append(total / len(gradeslist))
NameError: name 'gradeslist' is not defined
>>> pas[] = average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
SyntaxError: invalid syntax
>>> average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
  File "/home/karlo/Desktop/pythoni/nested list.py", line 39, in average
    averages.append(total / len(gradeslist))
NameError: name 'gradeslist' is not defined
>>> nova_list[] = average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
SyntaxError: invalid syntax
>>> grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]
>>> lista = average(grades)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lista = average(grades)
  File "/home/karlo/Desktop/pythoni/nested list.py", line 39, in average
    averages.append(total / len(gradeslist))
NameError: name 'gradeslist' is not defined
>>> 
[DEBUG ON]
>>> grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]
[DEBUG ON]
>>> lista = average(grades)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lista = average(grades)
  File "/home/karlo/Desktop/pythoni/nested list.py", line 39, in average
    averages.append(total / len(grades_list))
NameError: name 'gradeslist' is not defined
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
= RESTART: /home/karlo/Desktop/pythoni/nested list.py
>>> grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]
>>> lista = average(grades)
>>> lista
[75.0, 85.0, 90.0]
>>> flanders_filename = '/home/karlo/Desktop/pythoni/In Flanders Fields.txt'
>>> flanders_file = open (flanders_filename, 'r')
>>> flanders_file.readline()
'In Flanders Fields\n'
>>> flanders_file.readline()
'\n'
>>> flanders_file.readline()
'In Flanders fields the poppies blow\n'
>>> flanders_file.readline()
'Between the crosses, row on row,\n'
>>> flanders_file.readline()
'That mark our place; and in the sky\n'
>>> flanders_file.readline()
'The larks, still bravely singing, fly\n'
>>> flanders_file.readline()
'Scarce heard amid the guns below.\n'
>>> flanders_file.readline()
'\n'
>>> flanders_file.readline()
'We are the Dead. Short days ago\n'
>>> flanders_file.readline()
'We lived, felt dawn, saw sunset glow,\n'
>>> flanders_file.readline()
'Loved and were loved, and now we lie\n'
>>> flanders_file.readline()
'In Flanders fields.\n'
>>> flanders_file.readline()
'\n'
>>> flanders_file.readline()
'Take up our quarrel with the foe:\n'
>>> flanders_file.readline()
'To you from failing hands we throw\n'
>>> flanders_file.readline()
'The torch; be yours to hold it high.\n'
>>> flanders_file.readline()
'If ye break faith with us who die\n'
>>> flanders_file.readline()
'We shall not sleep, though poppies grow\n'
>>> flanders_file.readline()
'In Flanders fields.\n'
>>> flanders_file.readline()
'\n'
>>> flanders_file.readline()
'-John McCrae\n'
>>> flanders_file.readline()
''
>>> flanders_file.readline()
''
>>> flanders_file.readline()
''
>>> flanders_file.readline()
''
>>> flanders_file.readline()
''
>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> line = flanders_file.readline()
>>> while line != '':
	print(line)
	line = flanders_file.readline()

In Flanders Fields



In Flanders fields the poppies blow

Between the crosses, row on row,

That mark our place; and in the sky

The larks, still bravely singing, fly

Scarce heard amid the guns below.



We are the Dead. Short days ago

We lived, felt dawn, saw sunset glow,

Loved and were loved, and now we lie

In Flanders fields.



Take up our quarrel with the foe:

To you from failing hands we throw

The torch; be yours to hold it high.

If ye break faith with us who die

We shall not sleep, though poppies grow

In Flanders fields.



-John McCrae

>>> flanders_file.close()
>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> line = flanders_file.readline()
>>> while line != '':
	print(line)
	line = flanders_file.readline()
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> flanders_file = open(flanders_filename, 'r')
>>> line = flanders_file.readline()
>>> while line != '':
	print(line)
	line = flanders_file.readline()
	
SyntaxError: invalid syntax
>>> flanders_file = open(flanders_filename, 'r')

>>> line = flanders_file.readline()
>>> while line != '':
	print(line)
	line = flanders_file.readline()
	
KeyboardInterrupt
>>> while line != '':
	print(line, end = '')
	line = flanders_file.readline()

In Flanders Fields

In Flanders fields the poppies blow
Between the crosses, row on row,
That mark our place; and in the sky
The larks, still bravely singing, fly
Scarce heard amid the guns below.

We are the Dead. Short days ago
We lived, felt dawn, saw sunset glow,
Loved and were loved, and now we lie
In Flanders fields.

Take up our quarrel with the foe:
To you from failing hands we throw
The torch; be yours to hold it high.
If ye break faith with us who die
We shall not sleep, though poppies grow
In Flanders fields.

-John McCrae
>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> line = flanders_file.readline()
>>> line = flanders_file.readline()
>>> line = flanders_file.readline()
>>> line
'In Flanders fields the poppies blow\n'
>>> while line != '\n':
	print(line)
	line = flanders_file.readline()

In Flanders fields the poppies blow

Between the crosses, row on row,

That mark our place; and in the sky

The larks, still bravely singing, fly

Scarce heard amid the guns below.

>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> for line in flanders_file:
	print(line, end = '')

In Flanders Fields

In Flanders fields the poppies blow
Between the crosses, row on row,
That mark our place; and in the sky
The larks, still bravely singing, fly
Scarce heard amid the guns below.

We are the Dead. Short days ago
We lived, felt dawn, saw sunset glow,
Loved and were loved, and now we lie
In Flanders fields.

Take up our quarrel with the foe:
To you from failing hands we throw
The torch; be yours to hold it high.
If ye break faith with us who die
We shall not sleep, though poppies grow
In Flanders fields.

-John McCrae
>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> print(flanders_file.read())
In Flanders Fields

In Flanders fields the poppies blow
Between the crosses, row on row,
That mark our place; and in the sky
The larks, still bravely singing, fly
Scarce heard amid the guns below.

We are the Dead. Short days ago
We lived, felt dawn, saw sunset glow,
Loved and were loved, and now we lie
In Flanders fields.

Take up our quarrel with the foe:
To you from failing hands we throw
The torch; be yours to hold it high.
If ye break faith with us who die
We shall not sleep, though poppies grow
In Flanders fields.

-John McCrae

>>> flanders_file.close()
>>> flanders_file = open(flanders_filename, 'r')
>>> flanders_file.readlines()
['In Flanders Fields\n', '\n', 'In Flanders fields the poppies blow\n', 'Between the crosses, row on row,\n', 'That mark our place; and in the sky\n', 'The larks, still bravely singing, fly\n', 'Scarce heard amid the guns below.\n', '\n', 'We are the Dead. Short days ago\n', 'We lived, felt dawn, saw sunset glow,\n', 'Loved and were loved, and now we lie\n', 'In Flanders fields.\n', '\n', 'Take up our quarrel with the foe:\n', 'To you from failing hands we throw\n', 'The torch; be yours to hold it high.\n', 'If ye break faith with us who die\n', 'We shall not sleep, though poppies grow\n', 'In Flanders fields.\n', '\n', '-John McCrae\n']
>>> 
