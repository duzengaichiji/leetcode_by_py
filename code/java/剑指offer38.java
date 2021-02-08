class Solution {
    public void backtrack(String s,int index,int length,boolean[] used,char[] path,List<String> res){
        if(index==length){
            res.add(String.valueOf(path));
            return;
        }
        for(int i=0;i<length;i++){
            if(!used[i]){
                if(i>0&&s.charAt(i)==s.charAt(i-1)&&!used[i-1]) continue;
                used[i]=true;
                path[index]=s.charAt(i);
                backtrack(s,index+1,length,used,path,res);
                used[i]=false;
                path[index] = '#';
            }
        }
    }

    public String[] permutation(String s) {
        List<String> res = new ArrayList<>();
        boolean[] used = new boolean[s.length()];
        char[] path = new char[s.length()];
        for(int i=0;i<s.length();i++){
            used[i] = false;
            path[i] = '#';
        }
        backtrack(s,0,s.length(),used,path,res);
        String[] result = new String[res.size()];
        res.toArray(result);
        return result;
    }
}