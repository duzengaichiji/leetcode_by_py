class Solution:
    def rob(self, root: TreeNode) -> int:
        #memo = dict()
        def robTree(root):
            if root is None:
                return 0,0
            left,leftNon = robTree(root.left)
            right,rightNon = robTree(root.right)
            res = leftNon+rightNon+root.val
            resNon = max(left,leftNon)+max(rightNon,right)
            return res,resNon
        res,resNon = robTree(root)
        return max(res,resNon)