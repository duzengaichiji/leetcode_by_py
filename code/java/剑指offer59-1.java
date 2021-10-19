class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] result = new int[nums.length-k+1];
        if(nums.length==0) return new int[0];
        Deque<Integer> deque = new LinkedList<>();
        for(int i=0;i<k;i++){
            while(!deque.isEmpty()&&deque.peekLast()<nums[i]) deque.pollLast();
            deque.offerLast(nums[i]);
        }
        result[0] = deque.peekFirst();
        for(int i=k;i<nums.length;i++){
            if(nums[i-k]==deque.peekFirst()) deque.pollFirst();
            while(!deque.isEmpty()&&deque.peekLast()<nums[i]) deque.pollLast();
            deque.offerLast(nums[i]);
            result[i-k+1] = deque.peekFirst();
        }
        return result;
    }
}