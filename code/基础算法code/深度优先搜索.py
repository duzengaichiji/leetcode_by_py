
"""
深度优先搜索属于暴力解法，复杂度和搜索范围直接相关，通常为O(n)
通常只在数据范围小的时候适用；
"""

nums = []
used = [False ] *len(nums)

def backtrack(nums,idx,neighbor_map,used,target):
    """

    :param nums: 搜索范围
    :param idx: 当前索引
    :param neighbor_map: 邻接图，表示元素之间的关系
    :param used: 用来表示nums中的元素是否被搜索过
    :param target: 目标值
    :return:
    """
    # 找到目标，返回
    if nums[idx]==target:
        return True
    # 该idx要被标记为 “搜索过了”
    used[idx] = True
    # 取得当前idx的邻接图
    neighbors = neighbor_map[idx]
    # 在邻接图中搜索
    for member in neighbors:
        # 如果该member没有被搜索过，则递归进行搜索
        if not used[member]:
            if backtrack(nums,member,neighbor_map,used,target):
                return True
    # 所有元素均搜索过了，且未找到结果
    return False