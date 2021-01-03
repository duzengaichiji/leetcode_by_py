class Solution {
    public int fib(int n) {
        if(n<=1) return n;
        if(n<=2) return 1;

        long a = 0;
        long b = 1;
        for(long i=2;i<=n;i++){
            long temp = b;
            b = (b+a)%((long)1e9+7);
            a = temp;
        }
        return (int)b;
    }
}