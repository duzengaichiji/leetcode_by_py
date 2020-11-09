class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 两个候选人以及他们的当前票数
        a,b,count_a,count_b = 0,0,0,0
        res = []

        for i in nums:
            # 支持其中任意一个候选人，选票+1，其他不变
            if a==i:
                count_a+=1
                continue
            if b==i:
                count_b+=1
                continue
            # 不资瓷他们两个，则要判断是否变更当前候选人
            if count_a==0:
                a = i
                count_a = 1
                continue
            if count_b==0:
                b = i
                count_b = 1
                continue
            # 不资瓷两个当前候选人，他们的选票都-1
            count_a-=1
            count_b-=1
        # 验证阶段
        count_a,count_b = 0,0
        for j in nums:
            if j==a:
                count_a+=1
            elif j==b:
                count_b+=1
        if count_a>len(nums)/3:
            res.append(a)
        if count_b>len(nums)/3:
            res.append(b)
        return res