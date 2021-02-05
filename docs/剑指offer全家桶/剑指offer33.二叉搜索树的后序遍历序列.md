剑指offer33.二叉搜索树的后序遍历序列
----------
 - 题目
>输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
 - 示例
 ----------
> input: [1,6,3,2,5]
> 
> output: false
 ----------
 - 代码
 >
>
    class Solution:
        def verifyPostorder(self, postorder: List[int]) -> bool:
            midorder = sorted(postorder)
            print(midorder)
            def judege(mid_l,mid_r,post_l,post_r):
                if mid_l>mid_r:
                    return True
                # 如果当前序列只有一个元素，判断它们在前序和中序中是否相等
                if mid_l==mid_r:
                    return midorder[mid_l]==postorder[post_l]
                # 以后序遍历的最后一个为分界点，分割中序序列
                root = postorder[post_r]
                i = mid_l
                while i<=mid_r:
                    if midorder[i]==root:
                        break
                    i+=1
                if i>mid_r:
                    return False
                left = judege(mid_l,i-1,post_l,post_l+(i-mid_l)-1)
                right = judege(i+1,mid_r,post_l+(i-mid_l),post_r-1)
                # print(mid_l,i-1,post_l,post_l+(i-mid_l)-1)
                # print(i+1,mid_r,post_l+(i-mid_l),post_r-1)
                # print(i,mid_l,mid_r,post_l,post_r,left,right)
                return left and right
            return judege(0,len(postorder)-1,0,len(postorder)-1)
    

    
  ----------
 - 解析
 > 知道了这棵树上的所有元素，就可以得到其中序遍历的序列（因为二叉搜索树的中序序列是顺序排列的）
 > 
> 之后依据树的中序，后序，看是否能构成一棵树即可；
> 
> 