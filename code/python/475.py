class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bisect(num,arr):
            left = 0
            right = len(arr)-1
            while left<right:
                mid = (left+right)//2
                if num==arr[mid]: return 0
                if arr[mid]<num: left=mid
                elif arr[mid]>num: right=mid-1
            if arr[left]<num: return num-arr[left]
            if left==0: return arr[left]-num
            return min(arr[left]-num,num-arr[left-1])

        heaters = sorted(heaters)
        res = []
        for h in houses:
            res.append(bisect(h,heaters))
        return max(res)