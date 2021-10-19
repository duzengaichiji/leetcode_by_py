class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        midorder = sorted(postorder)
        print(midorder)

        def judege(mid_l, mid_r, post_l, post_r):
            if mid_l > mid_r:
                return True
            if mid_l == mid_r:
                return midorder[mid_l] == postorder[post_l]

            root = postorder[post_r]
            i = mid_l
            while i <= mid_r:
                if midorder[i] == root:
                    break
                i += 1
            if i > mid_r:
                return False
            left = judege(mid_l, i - 1, post_l, post_l + (i - mid_l) - 1)
            right = judege(i + 1, mid_r, post_l + (i - mid_l), post_r - 1)
            # print(mid_l,i-1,post_l,post_l+(i-mid_l)-1)
            # print(i+1,mid_r,post_l+(i-mid_l),post_r-1)
            # print(i,mid_l,mid_r,post_l,post_r,left,right)
            return left and right

        return judege(0, len(postorder) - 1, 0, len(postorder) - 1)