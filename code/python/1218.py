class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = [1]*len(arr)
        numPos = {}
        for i in range(len(arr)):
            if arr[i]-difference in numPos:
                res[i] = max(res[i],res[numPos[arr[i]-difference][-1]]+1)
            if arr[i] not in numPos:
                numPos[arr[i]] = []
            numPos[arr[i]].append(i)
        print(res)
        return max(res)