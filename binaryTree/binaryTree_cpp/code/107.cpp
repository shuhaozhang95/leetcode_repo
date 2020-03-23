// 树的自底向上层次遍历，需要用一个vector记录里面每一层的点

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        int level = 0;
        vector<vector<int>> tempV;
        queue<TreeNode*> tempQ;
        if(!root) return tempV;
        tempQ.push(root);

        while(!tempQ.empty()) {
            int curNum = tempQ.size();
            vector<int> vecLevel;
            //proc all node of the same level
            for(;curNum > 0; curNum--) {
                TreeNode *q = tempQ.front();
                tempQ.pop();
                vecLevel.insert(vecLevel.end(), q->val);
                if(q && q->left) tempQ.push(q->left);
                if(q && q->right) tempQ.push(q->right);
            }
            tempV.insert(tempV.begin(), vecLevel);
            //level ++; 
        }
        return tempV;
    }
};