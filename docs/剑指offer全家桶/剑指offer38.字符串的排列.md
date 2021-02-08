剑指offer38.字符串的排列
----------
 - 题目
>输入一个字符串，打印出该字符串中字符的所有排列。 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
 - 示例
 ----------
> input: s = "abc"
> 
> output: ["abc","acb","bac","bca","cab","cba"]
 ----------
 - 代码
 >
>
    class Solution:
        def permutation(self, s: str) -> List[str]:
            res = set()
            def dfs(index,length,path,used):
                if index==length:
                    res.add("".join(path))
                    return
                for i in range(len(used)):
                    if used[i]==False:
                        used[i]=True
                        path.append(s[i])
                        dfs(index+1,length,path,used)
                        used[i]=False
                        path.pop()
            dfs(0,len(s),[],[False]*len(s))
            #print(res)
            return list(res)
>
> 解法二
> 
> 
    class Solution:
        def permutation(self, s: str) -> List[str]:
            def backtrack(str_list,depth,length,used,path,res):
                if depth==length:
                    res.append("".join(path.copy()))
                    return
                for i in range(length):
                    if used[i]==False:
                        if i>0 and str_list[i]==str_list[i-1] and not used[i-1]:
                            continue
                        used[i] = True
                        path.append(str_list[i])
                        backtrack(str_list,depth+1,length,used,path,res)
                        path.pop()
                        used[i] = False
            res = []
            path = []
            s = list(s)
            s = sorted(s)
            used = [False]*len(s)
            backtrack(s,0,len(s),used,path,res)
            #res = list(set(res))
            return res
  ----------
 - 解析
 > dfs求解所有全排列，然后用hashSet去除即可；
> 
> 更好的解法是在求解过程中，剔除重复的解；
> 
> 这就要求在求解过程中，知道什么情况会导致重复；
> 
> 如果画出dfs树就会发现，同层（深度）出现相同字符的时候，就会出现重复的分支，这种分支应该去除；
> 
    if i>0 and str_list[i]==str_list[i-1] and not used[i-1]:
        continue
>
> 这个判断条件的前半部分，用于发现重复元素，后半部分用于确保是同层的重复分支；
> 
>  因为str_list[i-1]一定已经被用于当前层过了；