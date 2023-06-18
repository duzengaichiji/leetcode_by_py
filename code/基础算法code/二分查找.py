
"""
二分查找只适用于查找的数组已经有序的情况；
时间复杂度为O(nlogn)
"""

def bisect(arr,target):
    """

    :param arr: 顺序数组
    :param target: 目标值
    :return:
    """
    # 搜索范围
    left,right = 0,len(arr)-1
    while left<=right:
        # 搜索范围的中间位置
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        # 如果中间的值大于目标值，目标值只会出现在中间值右边
        # 则接下来只需要在其左边搜索，所以将搜索范围右边界定为 mid-1
        if arr[mid]>target:
            right = mid-1
        else:
            # 反之，是中间值小于目标值的情况，修改左边界
            left = mid+1
    return -1
