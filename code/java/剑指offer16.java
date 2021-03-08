class Solution {
    public double pow(double x,int n){
        if(n==0) return 1;
        if(n==1) return x;
        if(n%2==0) return pow(x*x,n/2);
        if(n%2!=0) return x*pow(x*x,n/2);
        return 0;
    }

    public double myPow(double x, int n) {
        if(n>=0) return pow(x,n);
        else return 1.0/pow(x,-1*n);
    }
}