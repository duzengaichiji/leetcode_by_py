class Solution {
    public int findNthDigit(int n) {
        if(n<10) return n;
        int digit = 1;
        int start = 1;
        int count = 9;
        while(n>count){
            n-=count;
            start*=10;
            digit+=1;
            count=9*start*digit;
        }
        int num = start+(n-1)/digit;
        String s = String.valueOf(num);
        int res = Integer.parseInt(String.valueOf(s.charAt((n-1)%digit)));
        return res;
    }
}