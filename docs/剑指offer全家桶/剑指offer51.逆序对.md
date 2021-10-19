剑指offer51.逆序对
----------
- 题目
> 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
> 
----------
- 示例
> input = [7,5,6,4]
> output = 5
----------
- 代码
>
    class Solution:
        def reversePairs(self, nums: List[int]) -> int:
            def mergeSort(tmp,start,end):
                if start>=end:
                    return 0
                mid = start+(end-start)//2
                count = mergeSort(tmp,start,mid)+mergeSort(tmp,mid+1,end)
                i,j,pos = start,mid+1,start
                # 归并排序
                while i<=mid and j<=end:
                    # nums[mid:j]都比nums[i]要小，所以计数是(j-(mid+1))
                    if nums[i]<=nums[j]:
                        tmp[pos] = nums[i]
                        i+=1
                        count += (j-(mid+1))
                    else:
                        tmp[pos] = nums[j]
                        j+=1
                    pos+=1
                while i<=mid:
                    # 剩下的是左半边，所以剩下的部分比右半边的全部都大，所以计数是(end-(mid+1))，此时j就是end
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
----------
 - 解析
 > 参考327.区间和的个数，这类求数组中任意点对[i,j]满足某种条件的题目，都可以采用归并排序进行优化；
>
> 套用归并排序的框架，并加入逆序对的计数部分即可；
>
> 对于任意两个已排好序的子数组，假设为leftP，表示原数组的nums[left:mid],和rightP，表示原数组的nums[mid+1:right]
>
> leftP[i]如果大于rightP[j]，则可以表明leftP[i]>rightP[mid+1:j]的全部；
>
> 因此，每次归并需要找到每个leftP[i]<=rightP[j]的最小的j，此时，rightP[mid+1:j]都是比leftP[i]小的，这些点和leftP[i]都能组成逆序对；
>