class Solution {
    private int index = 0;
    private boolean scanUnsignedInteger(String str){
        int before = index;
        while(str.charAt(index)>='0'&&str.charAt(index)<='9') index++;
        return index>before;
    }

    private boolean scanInteger(String str){
        //跳过符号部分
        if(str.charAt(index)=='+'||str.charAt(index)=='-') index++;
        return scanUnsignedInteger(str);
    }

    public boolean isNumber(String s) {
        //空串
        if(s==null||s.length()==0) return false;
        //加入结束标志
        s = s+'|';
        //跳过开头的空格
        while(s.charAt(index)==' ') index++;
        //判断是否包含整数部分，整数部分是否是数字
        boolean numeric = scanInteger(s);
        if(s.charAt(index)=='.'){
            //存在小数部分
            index++;
            //判断小数部分是否是数字
            numeric = scanUnsignedInteger(s)||numeric;
        }
        //判断'e'后面的是否是数字
        if((s.charAt(index)=='E'||s.charAt(index)=='e')){
            index++;
            numeric = numeric&&scanInteger(s);
        }
        //跳过后面的空格
        while(s.charAt(index)==' ') index++;
        return numeric&&s.charAt(index)=='|';
    }
}