class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if not arr: return 0
        # 0表示[0,0]即第一个元素自己亦或自己
        res = [0]
        for num in arr:
            res.append(res[-1]^num)

        count = 0
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)):
        #         for k in range(j,len(arr)):
        #             if res[i]==res[k+1]:
        #                 count+=1
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if res[i]==res[j+1]:
                    count+=j-i
        return count