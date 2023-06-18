class Solution {
    public List<String> restorIpLenX(String pre_s,String s,int ip_num,int zero_num){
        List<String> result = new ArrayList<>();
        if(ip_num==1){

            if(s.length()==1){
                result.add(pre_s+s);
                return result;
            }
            else if(Integer.parseInt(s)<255&&Integer.parseInt(s.substring(0,1))>0){
                result.add(pre_s+s);
                return result;
            }
            //return result;
        }
        else{
            List<String> result_t = new ArrayList<>();
            if(s.length()>=ip_num&&s.length()<=(ip_num-1)*3+1){
                if(Integer.parseInt(s.substring(0,1))==0){
                    if(zero_num==-1||Math.abs(ip_num-zero_num)>1){
                        zero_num=ip_num;
                        result_t = restorIpLenX(pre_s+s.substring(0,1)+".",s.substring(1,s.length()),ip_num-1,zero_num);
                        for(int i=0;i<result_t.size();i++)
                            result.add(result_t.get(i));
                    }
                }
                else if(Integer.parseInt(s.substring(0,1))>0){
                    result_t = restorIpLenX(pre_s+s.substring(0,1)+".",s.substring(1,s.length()),ip_num-1,zero_num);
                    for(int i=0;i<result_t.size();i++)
                        result.add(result_t.get(i));
                }
            }
            if(s.length()>=ip_num+1&&s.length()<=(ip_num-1)*3+2){
                if(Integer.parseInt(s.substring(0,2))>0&&Integer.parseInt(s.substring(0,1))>0){
                    result_t = restorIpLenX(pre_s+s.substring(0,2)+".",s.substring(2,s.length()),ip_num-1,zero_num);
                    for(int i=0;i<result_t.size();i++)
                        result.add(result_t.get(i));
                }
            }
            if((s.length()>=ip_num+2&&s.length()<=(ip_num-1)*3+3)&&Integer.parseInt(s.substring(0,3))<=255){
                if(Integer.parseInt(s.substring(0,3))>0&&Integer.parseInt(s.substring(0,1))>0){
                    result_t = restorIpLenX(pre_s+s.substring(0,3)+".",s.substring(3,s.length()),ip_num-1,zero_num);
                    for(int i=0;i<result_t.size();i++)
                        result.add(result_t.get(i));
                }
            }
        }
        return result;
    }

    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if(s.equals("0000")){
            result.add("0.0.0.0");
            return result;
        }
        if(s.equals("255255255255")){
            result.add("255.255.255.255");
            return result;
        }
        result = restorIpLenX("",s,4,-1);
        return result;
    }
}