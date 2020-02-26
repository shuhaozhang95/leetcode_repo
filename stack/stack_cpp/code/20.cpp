// 判断括号是否有效。即遍历字符串的字符，如果stack为空则讲字符加入stack。
// 若top element of stack跟当前元素配对则pop出。
// 若无匹配，继续加入stack。最后返回stack是否为空。

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