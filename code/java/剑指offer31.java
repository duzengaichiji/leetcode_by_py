class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int push_i = 0;
        int pop_i = 0;
        while(push_i<pushed.length||pop_i<popped.length){
            if(stack.size()==0||stack.peek()!=popped[pop_i]){
                if(push_i>=pushed.length) return false;
                stack.push(pushed[push_i]);
                push_i++;
            }else{
                if(stack.size()>0){
                    stack.pop();
                    pop_i+=1;
                }else return false;
            }
        }
        return true;
    }
}