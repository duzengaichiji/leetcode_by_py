class Solution {
    public int reverse(int x) {
        int sign = 1;
        ArrayList<Integer> result = new ArrayList();
        if(x<0){
            sign=-1;
            x = x*-1;
        }
        while(x>0){
            result.add(x%10);
            x = x/10;
        }
        //Collections.reverse(result);
        int res = 0;
        for(int i=0;i<result.size();i++){
            res = res*10+result.get(i);
            if(res>Integer.MAX_VALUE/10&&i!=result.size()-1)
                return 0;
        }
        return res*sign;
    }
}