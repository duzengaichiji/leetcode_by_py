
class Solution {
    public int largestRectangleArea(int[] heights) {
        int[] heightsWithZero = new int[heights.length+1];
        heightsWithZero[heights.length] = 0;
        for(int i=0;i<heights.length;i++) heightsWithZero[i] = heights[i];

        Stack stack = new Stack();
        int res = 0;
        int index = 0;

        ////System.out.println(Arrays.toString(heightsWithZero));

        while(index<heightsWithZero.length){
            if(stack.empty()||heightsWithZero[index]>heightsWithZero[(int)stack.peek()]){
                stack.push(index);
                index+=1;
            }
            else{
                int cur = (int)stack.pop();
                res = Math.max(res,heightsWithZero[cur]*(stack.size()==0?index:index-(int)stack.peek()-1));
            }
        }
        return res;
    }
}