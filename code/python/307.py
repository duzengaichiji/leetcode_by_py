class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0]*(self.n*2)
        # initialization
        for i in range(self.n):
            self.tree[self.n+i] = nums[i]
        for i in range(self.n-1,-1,-1):
            self.tree[i] = self.tree[i*2]+self.tree[2*i+1]
        #print(self.tree)

    def update(self, i: int, val: int) -> None:
        i+=self.n
        self.tree[i] = val
        while i>0:
            left = i
            right = i
            # 当前节点是其父节点的左还是右儿子
            if i%2==0:
                right = i+1
            else:
                left = i-1
            self.tree[i//2] = self.tree[left]+self.tree[right]
            i//=2

    def sumRange(self, i: int, j: int) -> int:
        i+=self.n
        j+=self.n
        res = 0
        while i<=j:
            if i%2==1:
                res+=self.tree[i]
                i+=1
            if j%2==0:
                res+=self.tree[j]
                j-=1
            i//=2
            j//=2
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)