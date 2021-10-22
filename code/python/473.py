class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 不能够成正方形
        if sum(matchsticks)%4!=0: return False
        sideLimit = sum(matchsticks)//4
        summation = sum(matchsticks)
        # 倒排，剪枝
        matchsticks = sorted(matchsticks)[::-1]
        def dfs(index,sides):
            # 火柴棍全部用完
            if index==len(matchsticks):
                return len(Counter(sides))==1
            # 找到当前火柴棍可以插入的边
            for i in range(len(sides)):
                # 当前火柴棍插入第i条边，会超过上限
                # 存在重复的边则跳过，直接去最后一条进行递归
                if sides[i]+matchsticks[index]>sideLimit or (i>0 and sides[i]==sides[i-1]):
                    continue
                # 当前火柴棍可以插入第i条边
                sides[i]+=matchsticks[index]
                #
                if dfs(index+1,sides):
                    return True
                sides[i]-=matchsticks[index]
            return False
        return dfs(0,[0]*4)