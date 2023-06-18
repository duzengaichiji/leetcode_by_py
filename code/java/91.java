class Solution {
    public int numDecodings(String s) {
        if(s.charAt(0)=='0')
            return 0;
        if(s.length()==1)
            return 1;
        int result = 0;
        int single = 0;
        int temp = 0;
        for(int i=0;i<s.length();i++){
            if(i==0){
                result=1;
                single=1;
            }
            else{
                if(s.charAt(i)!='0'){
                    temp = single;
                    single = result;
                    if(Integer.parseInt(s.substring(i-1,i+1))<=26&&s.charAt(i-1)!='0')
                        result+=temp;
                }
                else{
                    if(Integer.parseInt(s.substring(i-1,i+1))<=26){
                        result = single;
                        single = 0;
                    }
                    else{
                        return 0;
                    }
                }
            }
        }
        return result;
    }
}