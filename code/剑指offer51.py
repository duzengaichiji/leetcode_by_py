class Solution:
    def reversePairs(self, nums) -> int:
        def mergeSort(tmp,start,end):
            if start>=end:
                return 0
            mid = start+(end-start)//2
            count = mergeSort(tmp,start,mid)+mergeSort(tmp,mid+1,end)
            i,j,pos = start,mid+1,start
            while i<=mid and j<=end:
                if nums[i]<=nums[j]:
                    tmp[pos] = nums[i]
                    i+=1
                    count += (j-(mid+1))
                else:
                    tmp[pos] = nums[j]
                    j+=1
                pos+=1
            while i<=mid:
                tmp[pos] = nums[i]
                count+=(j-(mid+1))
                i+=1
                pos+=1
            while j<=end:
                tmp[pos] = nums[j]
                pos+=1
                j+=1
            nums[start:end+1] = tmp[start:end+1]
            return count
        tmp = [0]*len(nums)
        res = mergeSort(tmp,0,len(nums)-1)
        return res