# Notes for the LC Problem and Links to the `.py` file

### No.155 [Min Stack](https://leetcode.com/problems/min-stack/)

[Link to the Python file](./stack_python_code/155_Min_Stack.py)

**Notes**: 

* Use `min` funciton in python is possible but slow

* We could initialize a `min` variable when the class is implemented and the variable will be updated if a new int **push** to the stack is the new minimum. 

* The `min` will be append to the stack at first if the number will be pushed is less than or equal to the current minimum ==> <u>this is for consistant of minimum when pop occur</u>

* `max int` and `min int` in `python3`, 

``` python
import sys 

INT_MAX = sys.maxsize # sys.maxint for python2

INT_MIN = -sys.maxsize-1 
```


