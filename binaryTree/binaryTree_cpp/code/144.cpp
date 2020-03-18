// 树的前序遍历 思路相似
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
    vector<int> preorderTraversal(TreeNode* root) {
   	    if(root == NULL){
    		return res;
    	}  
        res.push_back(root->val);
    	if(root->left) preorderTraversal(root->left);
    	
    	if(root->right) preorderTraversal(root->right);
        return res;
    }
};
