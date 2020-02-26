/*
对于一个高度，如果能得到向左和向右的边界
那么就能对每个高度求一次面积
遍历所有高度，即可得出最大面积
*/
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        // st记录heights的index
        vector<int> st;
        // 在heights的最前与最后插入0，保证数组能够运行
        heights.insert(heights.begin(), 0);
        heights.push_back(0);
        // 遍历数组，从左开始，遍历到当前位置时，只用考虑当前位置向左的面积。向右的面积是后面的index来考量。
        for(int i=0; i<heights.size(); i++){
            // 维护一个单调递增栈，当当前高度小于栈顶时，则要push出来，凡是push出一个高度就要计算这个高度的面积。
            while(!st.empty() && heights[st.back()] > heights[i]){
                int cur = st.back();
                st.pop_back();
                int left = st.back() + 1;
                int right = i - 1;
                ans = max(ans, (right - left + 1)*heights[cur]);
            }
            st.push_back(i);
        }
        return ans;
    }
};