class Solution {
    public String replaceSpace(String s) {
        StringBuilder sb = new StringBuilder("");
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!=' ') sb.append(s.charAt(i));
            else sb.append("%20");
        }
        return sb.toString();
    }
}