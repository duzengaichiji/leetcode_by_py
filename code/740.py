class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        counts = collections.Counter(nums)
        counts = sorted(counts.items(),key = lambda x:x[0])
        dp_i_0 = 0 # i不取
        dp_i_1 = 0 # i取
        parts = [[]]
        last = None
        for num,count in counts:
            if last is None:
                parts[-1].append((num,count))
                last = num
            else:
                if num-1==last:
                    parts[-1].append((num,count))
                else:
                    parts.append([])
                    parts[-1].append((num,count))
                last = num

        def calRes(arr):
            if len(arr)==0: #孤立元素
                return arr[0][0]*arr[0][1]
            else:
                dp_i_0 = 0 # 当前位置不取
                dp_i_1 = 0 # 当前位置取
                for i in range(len(arr)):
                    temp = dp_i_0
                    dp_i_0 = max(dp_i_0,dp_i_1)
                    dp_i_1 = temp+arr[i][0]*arr[i][1]
                return max(dp_i_0,dp_i_1)

        res = 0
        for part in parts:
            res+=calRes(part)
        return res