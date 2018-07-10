## The ```>>>``` prompt

- Open the Anaconda Prompt (usually located at C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit))
-type
```
activate <nameOfEnvironment>
```
- type
```
python
```
- check the version
- You will see the python prompt ```>>>```.
- type and hit <kbd>Enter</kbd>

*Variabels*
```
>>> a = 3
>>> b = 2.54
>>> s = "Frank"
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 3, 'b': 2.54, 's': 'Frank'}
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(s)
<class 'str'>
```
*Simple calculations*
```
>>> a + b
5.54
>>> a * b
7.62
>>> a ** b
16.28875859622752
>>> a + s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> b / a
0.8466666666666667
```
*Printing*
```
>>> print(s)
Frank
>>> print(a)
3
>>> print(b)
2.54
>>> print(s + b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not float
>>> print(s , b)
Frank 2.54
>>> print('Hello {name}!'.format(name=s))
Hello Frank!
>>> print('{x}'.format(x=b))
2.54
>>> print('{x:06.2f}'.format(x=b))
002.54
>>> print('{x:06.1f}'.format(x=b))
0002.5
>>> print('{y:06d}'.format(y=a))
000003
>>> print('Hello {name}! It's {x:2.1f} degree C outside'.format(name=s, x=b))
  File "<stdin>", line 1
    print('Hello {name}! It's {x:2.1f} degree C outside'.format(name=s, x=b))
                            ^
SyntaxError: invalid syntax
>>> print("Hello {name}! It's {x:2.1f} degree C outside".format(name=s, x=b))
Hello Frank! It's 2.5 degree C outside
```
*Importing a module and using it*
```
>>> import math
>>> math.log(a)
1.0986122886681098
>>> help(math.log)
Help on built-in function log in module math:

log(...)
    log(x[, base])

    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.
```
*A function*
```
>>> def myfunction(x, y):
...     result = math.log(x) ** y
...     return result
...
>>> print(myfunction(4,3.333))
2.970326823989039
```
*If-statements*
```
>>> if a > b:
...     print('a is larger than b')
... else:
...     print('a is smaller or equal to b')
...
a is larger than b
>>>
```
*Looping through a list*
```
>>> l = [[2,7.23],[56,0.22],[6.34534,88]]
>>> for i in l:
...     print(myfunction(i[0],i[1]))
...
0.07065909705899072
1.3584912411200292
2.9106918320706165e+23
>>>
```

For reference about ```format()``` check out [Pyformat](https://pyformat.info/).
