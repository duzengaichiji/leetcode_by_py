class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(N)}
        # 建立邻接关系表
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # 任意节点子树中节点的总个数(包括自己)
        nodeNum = [1] * N
        # 任意节点的距离和
        distSum = [0] * N

        # 求任意节点的子树中的所有距离和
        def postOrder(root, parent):
            neighbors = graph[root]
            for neighbor in neighbors:
                # 父节点不用求
                if neighbor == parent:
                    continue
                postOrder(neighbor, root)
                nodeNum[root] += nodeNum[neighbor]
                distSum[root] += nodeNum[neighbor] + distSum[neighbor]

        # 求子树外的所有距离和
        def preOrder(root, parent):
            neighbors = graph[root]
            for neighbor in neighbors:
                if neighbor == parent:
                    continue
                distSum[neighbor] = distSum[root] - nodeNum[neighbor] + (N - nodeNum[neighbor])
                preOrder(neighbor, root)

        postOrder(0, -1)
        # print(distSum)
        # print(nodeNum)
        preOrder(0, -1)

        return distSum