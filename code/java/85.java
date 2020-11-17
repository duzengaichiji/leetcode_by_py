class Solution {
    public int maximalRectangle(char[][] matrix) {
        if(matrix.length==0) return 0;
        int res = 0;
        int[] heights = new int[matrix[0].length];
        int row = matrix.length;
        int col = matrix[0].length;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(matrix[i][j]=='0') heights[j]=0;
                else heights[j]+=1;
            }
            res = Math.max(res,calArea(heights));
        }
        return res;
    }

    public int calArea(int[] heights){
        int res = 0;
        int[] heights_ = new int[heights.length+1];
        for(int i=0;i<heights.length;i++) heights_[i] = heights[i];
        Stack stack = new Stack();
        int index = 0;
        while(index<heights_.length){
            if(stack.empty()||heights_[index]>heights_[(int)stack.peek()]){
                stack.push(index);
                index++;
            }
            else{
                int cur = (int)stack.pop();
                res = Math.max(
                    res,
                    heights_[cur]*(stack.size()==0?index:index-(int)stack.peek()-1)
                );
            }
        }
        return res;
    }
}