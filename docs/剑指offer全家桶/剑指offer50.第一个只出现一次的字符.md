剑指offer50.第一个只出现一次的字符
----------
 - 题目
>在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
>
 - 示例
 ----------
> input: "abaccdeff"
> 
> output: "b"
 ----------
 - 代码
 >
>
    class Solution:
        def firstUniqChar(self, s: str) -> str:
            count = Counter(list(s))
            for char in s:
                if count[char]==1:
                    return char
            return " "
>
> 只遍历一轮
>
>
    class Solution {
        public char firstUniqChar(String s) {
            int[] count = new int[26];
            for(int i=0;i<s.length();i++){
                count[s.charAt(i)-'a']+=1;
            }
            for(int i=0;i<s.length();i++){
                if(count[s.charAt(i)-'a']==1) return s.charAt(i);
            }
            return ' ';
        }
    }
  ----------
 - 解析
 > 
> 