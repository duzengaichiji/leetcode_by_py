public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        String binres = Integer.toBinaryString(n);
        int res = 0;
        for(int i=0;i<binres.length();i++){
            if(binres.charAt(i)=='1') res+=1;
        }
        return res;
    }
}