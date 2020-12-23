class NumArray {
    int[] tree;
    int n;
    public NumArray(int[] nums) {
        if(nums.length>0){
            n = nums.length;
            tree = new int[n*2];

            for(int i=n,j=0;i<n*2;i++,j++){
                tree[i] = nums[j];
            }
            for(int i=n-1;i>0;--i){
                tree[i] = tree[i*2]+tree[i*2+1];
            }
        }
    }

    public void update(int i, int val) {
        i+=n;
        tree[i] = val;
        while(i>0){
            int left = i;
            int right = i;
            if(i%2==0){
                right = i+1;
            }else{
                left = i-1;
            }
            tree[i/2] = tree[left]+tree[right];
            i/=2;
        }
    }

    public int sumRange(int l, int r) {
        l+=n;
        r+=n;
        int sum = 0;
        while(l<=r){
            // 考虑范围，左指针指向的是右节点时，只能加入右节点。
            if((l%2)==1){
                sum+=tree[l];
                l++;
            }
            // 右指针指向的是左节点时，只能加入左节点。
            if((r%2)==0){
                sum+=tree[r];
                r--;
            }
            //节点上移
            l/=2;
            r/=2;
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */