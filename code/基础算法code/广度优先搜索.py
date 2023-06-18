
"""
广度优先搜索属于暴力解法，复杂度和搜索范围直接相关，通常为O(n)
"""

def bfs(arr ,start ,target):
    """

    :param arr:要搜索的数组
    :param start:搜索起点
    :param target:目标值
    :return:
    """
    # 用来表示arr中的元素是否被搜索过
    used = [False ] *len(arr)
    # 标识起点为 已搜索过
    used[start] = True
    # 队列中放入
    queue = [start]
    while queue:
        # 每一轮搜索，会弹出队列中的第一个元素进行判断
        cur = queue.pop()
        if cur==target: # 已经到达目标
            return True
        for i in range(len(arr)):
            if used[i]==False:
                if Avaiable(arr[i]): # 判断 arr[i]是否可达
                    # 如果arr[i]可达，将它加入队列，纳入后续搜索范围
                    queue.append(arr[i])
    return False