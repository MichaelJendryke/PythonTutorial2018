# Python Tutorial (13-15 July)
In this tutorial you will get a brief introduction to Python programming. Even without prior knowledge of any programming language you should be able to follow along. Since the group is very small I will make this tutorial as interactive as possible. Most of the time you will be coding yourself to have as much hands-on experience as possible. As I do not know how fast/slow we will be able to move through the content I encourage you to think of a programming problem (from your research) yourself, which we will discuss and hopefully implement as well.

### Preparation
* Please visit [this webiste](http://www.learnpython.org/en/Welcome) and go through the examples in “Learn the Basics”. You can run the code online and do not need to install anything. We will repeat some of the exercises during the tutorial.

### Requirements
* A project or an idea what you would like to program that may help you with your research
* Anaconda for Python 3.6 (download the right version for your system from  [Anaconda](https://www.anaconda.com/download/)). We will install this together.

### Goals
Be able to set up your python programming environment; use command line arguments to read, modify and write files (text and images); plot graphs and figures; batch download data from the internet; and (if time permits) interact with a database.

### Suggested topics
(let me know if you want to cover additional topics)
1. Setup of Anaconda Environment
   - Creating a development environment
   - Package management
   - conda-forge
   - Text Editor or IDE?
2. How to read a documentation
3. The ```>>>``` prompt and basic built-in functions (```print()```, ```format()```, ```type()```, and ```help()```), see ```Python_Prompt.md```
4. Command line programs
   - Writing, formatting and organizing a ```*.py``` file, see ```basics.py```
   - Logging using ```logging```, see ```log.py```
   - Parsing command line arguments using ```argparse```, see ```arguments.py```
   - Parsing arguments using ```configparse```, see ```config.py```
   - “Hello Frank, it’s 12:39 on Tuesday March 15th, 2018” ```datetime```
5. Track your code changes with ```git```
6. Image time series using ```rasterstats``` and ```matplotlib``` (maybe also ```scikit-image```)
7. Batch download data with ```curl```
8. Student projects
9. (Database interaction)

## 1. Setup of Anaconda Environment

- Open the Anaconda Prompt (usually located at ```C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)``` on Windows)
- Go to [this](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/) website from Tsinghua University to add conda channels for China (this is only necessary, if you think the download speed for new packages is not fast enough)
- type:
   ```
   conda create -n <nameOfEnvironment> python=<version> <pakage>
   ```
This will create a development environment for you with the packages that you need and the python version you want. Press <kbd>y</kbd> when asked to proceed. You will see an output like this:
   ```
   #
   # To activate this environment, use:
   # > activate pytutorial36
   #
   # To deactivate an active environment, use:
   # > deactivate
   #
   # * for power-users using bash, you must source
   #
   ```
- Repeat the pervious two steps using a different name for the environment and a different python version
- type:
   ```
   activate <nameOfEnvironment>
   ```
- type:
   ```
   python
   ```
A short description of the current python version should appear
   ```
   Python 3.6.2 |Continuum Analytics, Inc.| (default, Jul 20 2017, 12:30:02) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```
- type:
   ```
   quit()
   ```
- To see information about the current environment type:
   ```
   conda info
   ```
- To see which packages are installed type:
   ```
   conda list
   ```
- To see all environments that you have created type:
   ```
   conda info --env
   ```

## 2. How to read a documentation
- Go to [python.org](https://docs.python.org/3/reference/index.html) and open the documentation for version 3.6

## 3. The ```>>>``` Prompt


- Open the Anaconda Prompt (usually located at ```C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)``` on Windows)
- To activate your environment type:
   ```
   activate <nameOfEnvironment>
   ```
- To start python type:
   ```
   python
   ```
- Check the version
- You will see the python prompt ```>>>```.
- Type and hit <kbd>Enter</kbd>

**Variabels**
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
**Simple calculations**
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
**Printing**
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
**Importing a module and using it**
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
**A function**
```
>>> def myfunction(x, y):
...     result = math.log(x) ** y
...     return result
...
>>> print(myfunction(4,3.333))
2.970326823989039
```
**If-statements**
```
>>> if a > b:
...     print('a is larger than b')
... else:
...     print('a is smaller or equal to b')
...
a is larger than b
>>>
```
**Looping through a list**

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

## 4. Command line programs
### ```basics.py```
- Follow along as I write the ```basics.py``` script
- Open Anaconda Prompt
- To activate your environment type:
   ```
   activate <nameOfEnvironment>
   ```
- Run the script by typing:
   ```
   python C:\Path\to\your\script\basics.py 2 3
   ```
- change directory to ```C:\Path\to\your\script\```
- type
   ```
   python
   ```
- type
   ```
   import basics
   ```
- type
   ```
   help(script)
   ```
- type
   ```
   help(script.myfunction)
   ```
- expand the script with
   - a function that tests, if ```a``` and ```b``` are equal
   - prints all numbers between ```a``` and ```b```.
   - tries to divide ```a``` and ```b``` (use a try statement in case ```b``` is 0)

### ```log.py```

See [this](https://docs.python.org/2/howto/logging.html) and [this](https://docs.python.org/3/library/logging.html) to learn how to use the logging module.

By setting the log level you can descide which messages should be printed out, they are ranked as follows.

* CRITICAL
* ERROR
* WARNING
* INFO
* DEBUG
* NOTSET

E.g if the log level is WARNING then ERROR and CRITICAL will also be printed.

:point_right: Check out how logging works in ```log.py```
- Follow along as I write the ```log.py``` script
- Task:
   - Create messages with different log levels.
   - Change the date format

### ```arguments.py```
- Follow along as I write the ```arguments.py``` script
- to see the usage of this script type:
   ```
   arguments.py -h
   ```
- Additional tasks: Use the described module ```argparse``` for all further scripts.

### ```config.py```
- Follow along as I write the ```config.py``` script
- Create the ```settings_1.cfg``` file
- ```configparse``` gives you the ability to run your script with different configurations.
- Task:
   - Change the script to supply the path to the config file using ```argparse```
   - Add an output directory and check if ```settings_1.cfg``` has an output path already

## 5. Track your code changes with ```git```
- Create an account at Github.com
- Install the Github Desktop Client
- Create a repository and sync it to github.com
- we will experiment a bit with ```git``` if we have time.

## 6. Image time series using ```rasterstats``` and ```matplotlib``` (maybe also ```scikit-image```)

- Follow along as I write the ```ndvi_timeseries.py``` script
- Tasks:
   - Add ```logging```
   - Add ```argparse``` or ```configparse```
   - Make your own shapefile (maybe try points instead of polygons)
   - Loop through the resulting time series data to make plots for every polygon

## 7. Batch download data with ```curl```
The task is to batch download data from a website.

- Go to [this](https://eol.jsc.nasa.gov/SearchPhotos/) website and search for images from the Intenational Space Station.
- If you do not want to search, you can click [this](//eol.jsc.nasa.gov/SearchPhotos/Technical.pl?SearchPublicCB=on&geon=Germany&SearchGeonCB=on) link.
- Down at the bottom is an option to download a Tab-Seperated Value (TSV) list of the search results. Download this file.
- Open your Anaconda prompt and activate your environment
- type
    ```
    conda install pycurl
    ```
- :point_right: Open your editor/IDE and write a script to download the images that are listed in the TSV file.
- Additional tasks:
    - Supply command line arguments for input TSV and output directory.
    - Only download images with a focal length higher than 50mm.
    - Unzip the files and sort them into folders by month.

## 8. Student projects
- I will allocate at least half day to help you with your research project\
