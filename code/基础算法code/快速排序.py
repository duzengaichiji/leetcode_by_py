
"""
快速排序每轮会确定一个元素在有序数组中的最终位置，然后递归的排序该元素的左右两边；

在数组乱序的时候，时间复杂度为 O(nlogn)；
当数组接近有序或者逆序时，复杂度为O(n²)；
"""

def fast_sort(arr,start,end):
    """

    :param arr: 待排序的数组
    :param start: 待排序部分的起点
    :param end: 待排序部分的终点
    :return:
    """
    # 记录起始点和终点
    left,right = start,end
    # 本轮确定最终位置的成员
    inc = arr[start]
    while left<right:
        # 右边比inc小的都移动到左边
        while left<right and arr[right]>inc:
            right-=1
        if left<right:
            arr[left] = arr[right]
            left+=1
        # 左边比inc小的都移动到右边
        while left<right and arr[left]<=inc:
            left+=1
        if left<right:
            arr[right] = arr[left]
            right-=1
    # 确定了inc的最终位置
    arr[right] = inc
    if start<right:
        # 排序inc左边的部分
        fast_sort(arr,start,right-1)
    if right<end:
        # 排序inc右边的部分
        fast_sort(arr,right+1,end)
    return
