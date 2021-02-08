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