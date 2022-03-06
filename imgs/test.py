def solution(lists:list):
    lists = sorted(lists,key = lambda x:x[0])
    res = 0
    cur = lists[0]
    for i in range(1,len(lists)):
        nextArea = lists[i]
        if nextArea[0]>=cur[1]:
            cur = nextArea
        else:
            res += 1
            if cur[1]>nextArea[1]:
                cur = nextArea
    return res

if __name__ == "__main__":
    sample = [[1,2],[2,3],[3,4],[1,3]]
    print(solution(sample))