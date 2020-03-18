// 树的后序遍历 思路类似
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
    vector<int> postorderTraversal(TreeNode* root) {
        if(root == NULL){
    		return res;
    	}  
    	if(root->left) postorderTraversal(root->left);
    	if(root->right) postorderTraversal(root->right);
        res.push_back(root->val);
        return res;
    }
};

