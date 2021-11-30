# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(left,right):
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            if left<=mid-1:
                node.left = build(left,mid-1)
            if mid+1<=right:
                node.right = build(mid+1,right)
            return node
        return build(0,len(nums)-1)
