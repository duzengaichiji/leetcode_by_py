class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        length = len(nums)
        minVal = min(nums)
        maxVal = max(nums)
        if maxVal-minVal==0:
            return 0
        #为了让桶的数量大于n-2,以n-1个桶来计算interval，保证一定有一个空的桶-->最大gap不会出现在桶内部的max-min中
        #每个箱子的范围
        if (maxVal-minVal)/(length-1)>(maxVal-minVal)//(length-1):
            interval = (maxVal-minVal)//(length-1)+1
        else:
            interval = (maxVal-minVal)//(length-1)
        #存放每个桶中的最大和最小值
        bucketMin = [float('inf')]*(length-1)
        bucketMax = [-1]*(length-1)

        for i in range(length):
            #计算nums[i]所在的桶的索引
            index = (nums[i]-minVal)//interval
            #不考虑最大和最小值
            if nums[i]==minVal or nums[i]==maxVal:
                continue
            #更新桶内的值
            bucketMin[index] = min(nums[i],bucketMin[index])
            bucketMax[index] = max(nums[i],bucketMax[index])

        print(interval)
        print(bucketMin)
        print(bucketMax)

        maxGap = 0
        #minVal视作第-1个箱子的最大值
        previousMax = minVal
        for i in range(length-1):
            if bucketMax[i]==-1:
                continue
            #当前桶的最小值减前一个桶的最大值
            maxGap = max(bucketMin[i]-previousMax,maxGap)
            previousMax = bucketMax[i]
        #maxVal-最后一桶的最大值
        maxGap = max(maxVal-previousMax,maxGap)
        return maxGap