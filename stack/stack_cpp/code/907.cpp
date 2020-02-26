/** 
Solution 1
前后单调栈方法
对于每个j，找到j左右两边都大于j的连续边界。就可以算出j贡献的，所以用2个单调栈去维护j的左右边界
然后再对每个j的边界进行加和
**/

class Solution {
public:
    int sumSubarrayMins(vector<int>& A) {
        long MOD = 1e9 + 7;
		int N = A.size();
        stack<int> st;
		vector<int> prev(N);
        for(int i=0;i<N;i++){
            while(!st.empty() && A[i] <= A[st.top()]){
                st.pop();
            }
            prev[i] = st.empty()? -1:st.top();
            st.push(i);
        }

        stack<int> right;
        vector<int> next_(N);
        for(int k= N-1;k>-1;k--){
            while(!right.empty() && A[k] < A[right.top()]){
                right.pop();
            }
            next_[k] = right.empty()? N:right.top();
            right.push(k);
        }

        long ans = 0;
        for(int j=0;j<N;j++){
            ans = ans + (j - prev[j])*(next_[j]-j)*(A[j]);
        }
        return ans % MOD;
    }
};




/** 
Solution_2 维护最小值栈

对于每个 j，考虑所有子序列 [i, j] 的最小值。想法是每当我们增加 j，这些最小值可能会有关联，事实上，min(A[i:j+1]) = min(A[i:j], A[j+1])。
模拟数组 A = [1,7,5,2,4,3,9]，当 j = 6 事所有子序列 [i, j] 的最小值为 B = [1,2,2,2,3,3,9]，可以发现重要点是 i = 0, i = 3, i = 5, i = 6 ，分别是从 j 开始向左移动遇到的最小值的位置。
维护关于重要点的编码 B，对于上面提到的 (A, j) 维护 stack = [(val=1, count=1), (val=2, count=3), (val=3, count=2), (val=9, count=1)]，这表示最小值的编码为 B = [1,2,2,2,3,3,9]。对于每个 j 我们需要计算 sum(B)。

即这里的stack用来存储（value, count）针对每个j， 当计算完一个j时，就计算当前j的sum.

当我们增加 j，我们用最新的元素 (val=x, count=1) 更新栈。弹出所有值 >= x 的元素，因为当前子序列 [i, j] 的最小值将是 A[j] 而不是之前的值。

最后，结果是栈元素的点积为[i,j]所有子序列的最小值, 用dot来维护 

**/
class Solution {
public:
    int sumSubarrayMins(vector<int>& A) {
        stack<pair<int, int>> stk;
        int sum = 0, dot = 0;
        const int MOD = 1e9 + 7;
        for (int i = 0; i < A.size(); i++) {
            int count = 1;

            // 如果新的j比栈顶的大，就弹出。重新计算当前的J的value, count pair
            while (!stk.empty() && A[i] <= stk.top().first) {
                auto top = stk.top();
                stk.pop();
                // 因为原来都是9的次数，被新的最小占据了，所以把次数加到新的最小上。
                count += top.second;
                // dot把原来多出来的去掉
                dot -= top.first * top.second;
            }
            dot += A[i] * count;
            stk.push(make_pair(A[i], count));
            // dot维护的是每个j的sum(B), 要把每个j的sum(B)加起来
            // 因为这里的sum(B)是必须以j结尾的
            sum += dot;
            sum %= MOD;
        }
        return sum;
    }
};


/**
Solution 2 的同样思路
**/ 

class Solution {
public:
    int sumSubarrayMins(vector<int>& A) {
        long long MOD = 1e9 + 7;
        stack<int> s;
        long long cur_sum = 0, ans = 0;
        for (int i = 0; i < A.size(); ++i) {
            while (!s.empty() && A[s.top()] >= A[i]) {
                int top = s.top(); s.pop();
                int new_top = s.empty() ? -1 : s.top();
                cur_sum += (A[i] - A[top]) * (top - new_top);
            }
            cur_sum += A[i];
            s.push(i);
            ans += cur_sum;
        }
        return ans % MOD;      
    }
};
