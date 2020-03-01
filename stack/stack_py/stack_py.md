# Notes for the LC Problem and Links to the `.py` file

### No.155 [Min Stack](https://leetcode.com/problems/min-stack/)

[Link to the Python file](./code/155_minStack.py)

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

---

### No.385 [Mini Parser](https://leetcode.com/problems/mini-parser/)

[Link to the Python file](./code/385_miniParser.py)

**Notes**:

* Could use [functools](https://docs.python.org/3/library/functools.html#functools.lru_cache) to help control the memeory and increase efficiency

e.g. `@functools.lru_cache(maxsize=128, typed=False)`


---

### No.856 [Sores of Parenthness](https://leetcode.com/problems/score-of-parentheses/)

[Link to the Python file](./code/856_scoreOfParentheses.py)

---

### No.907 [Sum of Subarray Mins](https://leetcode.com/problems/sum-of-subarray-minimums/)

[Link to the Python file](./code/907_sumSubarrayMins.py)

**Notes**:

* Use two methods whose concept is **important** and <u>might be helpful for other similar scenarios</u>
    - **[1]**: find the left and right boundary that the current num is the min of the subarray
    - **[2]**: maintain a stack of minimum value and counts 

---