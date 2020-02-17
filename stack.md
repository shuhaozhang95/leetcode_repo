## Stack in C++

堆栈是一个后进先出(Last In First Out)表，即 LIFO 表

C++ STL 的堆栈泛化是直接通过现有的序列容器来实现的，默认使用双端队列deque的数据结构，当然，可以采用其他线性结构（vector 或 list等），只要提供堆栈的入栈、出栈、栈顶元素访问和判断是否为空的操作即可。

stack的元素出栈操作是不返回栈顶元素的，需要另外通过取栈顶函数获得。这种分离实现是考虑到出栈函数若直接返回栈顶元素，将会导致返回值的数据引用安全问题或不必要的低效复制函数的调用。

从 stack 内部实现看，stack 堆栈是不设最大容量的，但可通过 size 函数获取当前堆栈的大小，以判断是否允许继续让元素入栈，实现具有最大容量限制的堆栈。

stack堆栈容器的C++标准头文件为 stack ，必须用宏语句 "#include <stack>" 包含进来，才可对 stack 堆栈的程序进行编译。

- stack<int> s; 创建一个空的stack对象

  stack(const stack&)
  复制构造函数，用一个 stack 堆栈创建一个新的堆栈。
  例如，下面的代码利用 s1 ，创建一个以双向链表为底层容器的空堆栈对象 s2 。
  // stack<int, list<int> >   s1;
  stack<int, list<int> >   s2(s1);

- empty() 堆栈为空则返回真

- pop() 移除栈顶元素
- push() 在栈顶增加元素
- size() 返回栈中元素数目
- top() 返回栈顶元素



### 20

判断括号是否有效。即遍历字符串的字符，如果stack为空则讲字符加入stack。若top element of stack跟当前元素配对则pop出。若无匹配，继续加入stack。最后返回stack是否为空。

```c++
class Solution {
public:
    bool isValid(string s) {
        int len = s.size();
        if(!len) return true;
        if(len%2==1) return false;
        stack<char> s1;
        for(int i=0;i<len;++i){
            if(s1.empty()){
                s1.push(s[i]);
                continue;
            }
            if(s1.top()=='[' && s[i]== ']'){
                s1.pop();
                continue;
            }
            if(s1.top()=='(' && s[i]== ')'){
                s1.pop();
                continue;
            }
            if(s1.top()=='{' && s[i]== '}'){
                s1.pop();
                continue;
            }
            s1.push(s[i]);
        }
        return s1.empty();
    }
};
```



### 907

https://leetcode-cn.com/problems/sum-of-subarray-minimums/

