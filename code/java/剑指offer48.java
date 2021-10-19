class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        Map<Character,Integer> map = new HashMap<>();
        int i = 0;
        int j = 0;
        while(j<s.length()){
            char c = s.charAt(j);
            if(!map.containsKey(c)){
                map.put(c,1);
                res = Math.max(res,j-i+1);
                j+=1;
            }
            else if(map.get(c)==0){
                map.remove(c);
                map.put(c,1);
                res = Math.max(res,j-i+1);
                j+=1;
            }
            else{
                while(i<j){
                    if(s.charAt(i)==s.charAt(j)){
                        map.remove(s.charAt(j));
                        break;
                    }
                    int temp = map.get(s.charAt(i));
                    map.remove(s.charAt(i));
                    map.put(s.charAt(i),temp-1);
                    i++;
                }
                i++;
            }
        }
        res = Math.max(res,j-i);
        return res;
    }
}