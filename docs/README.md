# General information
This library contains useful functions for comfortable implementation of geometry objects in your code.
For each geometric structure determined functions of finding `area` and `perimeter`
> Important! All the length values used as parameters in these function are non-negative as they are in the science of Math, the function will be throwing exception whether you try to input negative value.
> Important! The function of triangle **do not** check whether the values satisfy the triangle inequality.
### Geometric structures are:
- Circle
- Rectangle
- Square
- Triangle

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a*h/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Function description
## Circle
### Area
Implements finding the area of circle with radius equal to `r`.

_Parameters_: `r` (int, float, etc) - the value of radius \
_Return value_: `area` (float, etc) - the value of area of circle

```python
>>> circle.area(3)
>>> 28.274333882308138

>>> circle.area(5.5)
>>> 95.03317777109125
```
### Perimeter
Implements finding the perimiter of circle with radius equal r

_Parameters_: `r` (int, float, etc) - the value of radius \
_Return value_: `perimeter` (float, etc) - the value of perimiter of the circle

```python
>>> circle.perimeter(3)
>>> 18.84955592153876

>>> circle.perimeter(5.5)
>>> 34.55751918948772
```
## Rectangle
### Area
Implements finding the area of rectangle with sides lengths equal to `a` and `b`.

_Parameters_:  
`a` (int, float, etc) - one of the rectangle sides  
`b` (int, float, etc) - another rectangle side \
_Return value_:  
`area` (int, float, etc) - the value of area of rectangle

```python
>>> rectangle.area(2, 3)
>>> 6

>>> rectangle.area(2.5, 3.5)
>>> 8.75
```
### Perimeter
Implements finding the perimeter of rectangle with sides lengths equal to `a` and `b`.

_Parameters_:  
`a` (int, float, etc) - one of rectangle sides  
`b` (int, float, etc) - another rectangle side \
_Return value_:  
`perimeter` (int, float, etc) - the value of perimeter of rectangle

```python
>>> rectangle.perimeter(2, 3)
>>> 10

>>> rectangle.perimeter(2.1, 3.5)
>>> 11.8
```
## Square
### Area
Implements finding the area of square with side length equal to `a`.

_Parameters_: `a` (int, float, etc) - square side length \
_Return value_: `area` (int, float, etc) - the value of area of square

```python
>>> square.area(2)
>>> 4

>>> square.area(5.5)
>>> 30.25
```
### Perimeter
Implements finding the perimeter of square with side length equal to `a`.

_Parameters_: `a` (int, float, etc) - square side length \
_Return value_: `perimeter` (int, float, etc) - the value of perimeter of square

```python
>>> square.perimeter(2)
>>> 8

>>> square.perimeter(5.5)
>>> 22
```
## Triangle
### Area
Implements finding the area of triangle with side length equal to `a` and height `h` lowered to this side.

_Parameters_: `a` (int, float, etc) - triangle side length \
_Return value_: `area` (int, float, etc) - the value of area of triangle

```python
>>> triangle.area(4, 3)
>>> 6

>>> triangle.area(4, 5.4)
>>> 10.8
```
### Perimeter
Implements finding the perimeter of triangle with sides length equal to `a`, `b` and `c`. 

_Parameters_:  
`a` (int, float, etc) - triangle side length \
`b` (int, float, etc) - another triangle side length \
`c` (int, float, etc) - last triangle side length \
_Return value_:  
`perimeter` (int, float, etc) - the value of perimeter of triangle

```python
>>> triangle.perimeter(1, 2, 3)
>>> 6

>>> triangle.perimeter(2.5, 5.4, 4.5)
>>> 12.4
```
# Project history
```
* 80ddab9 (HEAD -> main) Testing implemented & some updates in markdown
* eab0dab Test directort created & exception throws implemented & markdown updates and fixing typos
* 04c1f53 (origin/new_features_lab2) documentation in markdown created docs/README.md\
* 74a1c00 (HEAD -> main, origin/new_features_lab2) typo fixes
* f9c29b7 description for every function added
* d755497 (origin/main, origin/HEAD) new file triangle.py added & method perimetr in rectangle.py fixed
* 6222860 new file rectangle.py added
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added
```
# Tests describtion
The library comes with full unit testing in directory: `geometric_lib\tests` using Python standart library `unittest`. Enabling unit tests on command `$ python.exe -m unittest <name of file>_test`
### Sources
> This markdown was created using [this useful GitHub Docs page](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)