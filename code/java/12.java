class Solution {
    public String intToRoman(int num) {
        String result = "";
        //千位
        int thousand = num/1000;
        for(int i =0;i<thousand;i++)
            result+="M";
        num = num%1000;
        //百位
        if(num>=900){
            result+="CM";
            num-=900;
        }
        else{
            if(num>=500&&num<900){
                result+="D";
                num-=500;
            }
            if(num>=400){
                result+="CD";
                num-=400;
            }
            else{
                int hundred = num/100;
                for(int i=0;i<hundred;i++)
                    result+="C";
                num = num%100;
            }
        }
        //十位
        if(num>=90){
            result+="XC";
            num-=90;
        }
        else{
            if(num>=50&&num<90){
                result+="L";
                num-=50;
            }
            if(num>=40){
                result+="XL";
                num-=40;
            }
            else{
                int ten = num/10;
                for(int i=0;i<ten;i++)
                    result+="X";
                num = num%10;
            }
        }
        //个位
        if(num>=9){
            result+="IX";
            num-=9;
        }
        else{
            if(num>=5&&num<9){
                result+="V";
                num-=5;
            }
            if(num>=4){
                result+="IV";
                num-=4;
            }
            else{
                for(int i=0;i<num;i++)
                    result+="I";
            }
        }
        return result;
    }
}