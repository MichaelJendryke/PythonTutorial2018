## Creating and Environment

- open the Anaconda Prompt (usually located at C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit))
- type
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
- repeat the pervious two steps using a different name for the environment and a different python version
- type
```
activate <nameOfEnvironment>
```
- type
```
python
```
a short description of the current python version should appear
```
Python 3.6.2 |Continuum Analytics, Inc.| (default, Jul 20 2017, 12:30:02) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
- type
```
quit()
```
