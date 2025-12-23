Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ord('a')
97
ord('Z')
90
s='sujith
SyntaxError: unterminated string literal (detected at line 1)
s='
SyntaxError: unterminated string literal (detected at line 1)
s='''
python
class
is
going
good
'''
s.splitlines()
['', 'python', 'class', 'is', 'going', 'good']
','.join(s)
'\n,p,y,t,h,o,n,\n,c,l,a,s,s,\n,i,s,\n,g,o,i,n,g,\n,g,o,o,d,\n'
' '.join(s)
'\n p y t h o n \n c l a s s \n i s \n g o i n g \n g o o d \n'
# spliting
s.partition(i)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.partition(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
s='python class is going well'
s.partition(i)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.partition(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
s.partition()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.partition()
TypeError: str.partition() takes exactly one argument (0 given)
s.partiction('')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.partiction('')
AttributeError: 'str' object has no attribute 'partiction'. Did you mean: 'partition'?
s.partition('')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.partition('')
ValueError: empty separator
s.partition('.')
('python class is going well', '', '')
s='  python    programmin  '
s.strip()
'python    programmin'
>>> s='  python    programming  '
>>> s.strip()
'python    programming'
>>> s.lstrip()
'python    programming  '
>>> s.rstrip()
'  python    programming'
>>> 
>>> #encoding and decodeing
>>> #encoding and decodeing
>>> s='python class is going well'
>>> s.encode()
b'python class is going well'
>>> s.decode()
Traceback (most recent call last):
... 
  File "<pyshell#38>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> k=s.encode()
>>> k
b'python class is going well'
>>> k.decode()
'python class is going well'
