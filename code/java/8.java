class Solution {
    public int myAtoi(String str) {
        if(str==null)
            return 0;
        int valid_pos = 0;
        while(valid_pos<str.length()){
            if(str.charAt(valid_pos)!=' ')
                break;
            else
                valid_pos++;
        }
        if(valid_pos==str.length()||(!Character.isDigit(str.charAt(valid_pos))&&str.charAt(valid_pos)!='-')&&str.charAt(valid_pos)!='+')
            return 0;
        else{
            int result = -1;
            int signal = 1;
            if(str.charAt(valid_pos)=='-'){
                signal=-1;
                valid_pos++;
            }
            else if(str.charAt(valid_pos)=='+'){
                signal=1;
                valid_pos++;
            }
            while(valid_pos<str.length()){
                if(Character.isDigit(str.charAt(valid_pos))){
                    if(result==-1)
                        result = 0;
                    if(signal==1&&(result>Integer.MAX_VALUE/10||(result==Integer.MAX_VALUE/10&&str.charAt(valid_pos)>'7')))
                       return Integer.MAX_VALUE;
                        //return result;
                    if(signal==-1&&(result>Integer.MAX_VALUE/10||(result==Integer.MAX_VALUE/10&&str.charAt(valid_pos)>'8')))
                       return Integer.MIN_VALUE;

                    result=result*10+Integer.parseInt(String.valueOf(str.charAt(valid_pos)));
                    valid_pos++;
                }
                else{
                    break;
                }
            }
            if(result==-1)
                return 0;
            return result*signal;
        }
    }
}