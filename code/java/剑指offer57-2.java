class Solution {
    public int[][] findContinuousSequence(int target) {
        List<int[]> res = new ArrayList<int[]>();
        int l=1,r=2;
        while(l<r){
            int sum = (l+r)*(r-l+1)/2;
            if(sum==target){
                int[] temp = new int[r-l+1];
                for(int i=l;i<=r;i++) temp[i-l] = i;
                res.add(temp);
                l++;
            }else if(sum<target) r++;
            else l++;
        }
        return res.toArray(new int[res.size()][]);
    }
}