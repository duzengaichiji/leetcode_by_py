class Solution {
    public int findRepeatNumber(int[] nums) {
        Map<Integer,Integer> numCount = new HashMap<>();
        for(int num:nums){
            if(numCount.containsKey(num)){
                int c = numCount.get(num);
                numCount.put(num,c+1);
            }else{
                numCount.put(num,1);
            }
        }

        Iterator iter = numCount.entrySet().iterator();
        while(iter.hasNext()){
            Map.Entry entry = (Map.Entry)iter.next();
            int key = (int)entry.getKey();
            int value = (int)entry.getValue();
            if(value>1) return key;
        }
        return 0;
    }
}