class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        def push(i,j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(h,[nums1[i]+nums2[j],i,j])
        # (i,0) 先全部推入堆中
        for i in range(min(k,len(nums1))):
            push(i,0)
        res = []
        while h and len(res)<k:
            # 最小组合
            _,i,j = heapq.heappop(h)
            res.append([nums1[i],nums2[j]])
            # 考虑有序，比(i,j)大的应是(i,j+1)
            push(i,j+1)
        return res

