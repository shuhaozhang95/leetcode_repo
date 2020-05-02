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
    bool isBalanced(TreeNode* root) {
        if(!root) return true;
        
        int d = abs(depth(root->left)-depth(root->right)); //当前节点的左右子树的高度差
        
        return (d<=1) && (isBalanced(root->left)) && (isBalanced(root->right));
    }
    
    // 求解二叉树深度（104题）
    int depth(TreeNode* node)
    {
        if(node ==NULL) return 0;
        return max( depth(node->left), depth(node->right) )+1;
    }
    
};