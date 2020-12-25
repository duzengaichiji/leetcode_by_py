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
    int ans = 0;    // 结果
    public int longestUnivaluePath(TreeNode root) {
        helper(root);
        return ans;
    }

    // 搜索以root为起点的最长同值路径
    // 要么经过左子树，要么经过右子树
    public int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int maxLength = 0;  // 以root为起点的最长同值路径
        int leftLength = helper(root.left);     // 以root.left为起点的最长同值路径
        int rightLength = helper(root.right);   // 以root.right为起点的最长同值路径
        // 情况2，不需要更新maxLength，但要更新结果
        if (root.left != null && root.right != null &&
            root.val == root.left.val && root.val == root.right.val) {
                ans = Math.max(ans, leftLength + rightLength + 2);
        }
        // 从左右子树中选取最长同值路径
        if (root.left != null && root.val == root.left.val) {
            maxLength = leftLength + 1;
        }
        if (root.right != null && root.val == root.right.val) {
            maxLength = Math.max(maxLength, rightLength + 1);
        }
        // 更新结果
        ans = Math.max(ans, maxLength);
        return maxLength;
    }
}

作者：zui-weng-jiu-xian
链接：https://leetcode-cn.com/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-di-gui-bian-li-by-zui-w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。