class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dictionary = {}
        for i in range(len(nums2)):
            dictionary[nums2[i]] = i

        stack = []
        bigger = [-1]*len(nums2)
        index = len(nums2)-1
        while index>-1:
            num = nums2[index]
            if not stack:
                bigger[index] = -1
                stack.append(num)
                index-=1
                continue
            elif stack[-1]>num:
                bigger[index] = stack[-1]
                stack.append(num)
                index-=1
                continue
            elif stack[-1]<num:
                stack.pop()
        for i in range(len(nums1)):
            if nums1[i] not in dictionary:
                res.append(-1)
            else:
                res.append(bigger[dictionary[nums1[i]]])
        return res
