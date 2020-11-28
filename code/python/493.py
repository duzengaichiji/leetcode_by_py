class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr, temp, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = mergeSort(arr, temp, left, mid) + mergeSort(arr, temp, mid + 1, right)
            # 计数部分
            li = mid
            ri = right
            while li >= left and ri >= mid + 1:
                if arr[li] > arr[ri] * 2:
                    count += (ri - mid)
                    li -= 1
                else:
                    ri -= 1
            # 排序部分
            i = left
            j = mid + 1
            index = left
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[index] = arr[i]
                    i += 1
                else:
                    temp[index] = arr[j]
                    j += 1
                index += 1
            while i <= mid:
                temp[index] = arr[i]
                i += 1
                index += 1
            while j <= mid:
                temp[index] = arr[j]
                j += 1
                index += 1
            nums[left:right + 1] = temp[left:right + 1]
            return count

        if not nums:
            return 0
        res = mergeSort(nums, nums.copy(), 0, len(nums) - 1)
        return res
