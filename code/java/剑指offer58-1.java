class Solution {
    public String reverseWords(String s) {
        String[] temp = s.split(" ");
        StringBuffer sb = new StringBuffer();
        for(int i=temp.length-1;i>=0;i--){
            if(temp[i].strip()!=""){
                sb.append(temp[i].strip());
                sb.append(" ");
            }
        }
        if(sb.length()>0) sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}