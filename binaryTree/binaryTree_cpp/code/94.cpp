// 树遍历的简单难度，主要是要理解迭代的思想。
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
    vector<int> res;
    vector<int> inorderTraversal(TreeNode* root) {
    	if(root == NULL){
    		return res;
    	}   
    	if(root->left) inorderTraversal(root->left);
    	res.push_back(root->val);
    	if(root->right) inorderTraversal(root->right);
        return res;
    }
};

