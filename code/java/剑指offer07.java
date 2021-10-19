/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildNode(int[] preorder,int preL,int preR,int[] inorder,int inL,int inR){
        if(preL>preR||inL>inR) return null;
        TreeNode newNode = new TreeNode(preorder[preL]);
        int i = 0;
        while(inorder[inL+i]!=preorder[preL]) i+=1;
        newNode.left = buildNode(preorder,preL+1,preL+i,inorder,inL,inL+i-1);
        newNode.right = buildNode(preorder,preL+i+1,preR,inorder,inL+i+1,inR);

        return newNode;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        TreeNode root = buildNode(preorder,0,preorder.length-1,inorder,0,inorder.length-1);
        return root;
    }
}