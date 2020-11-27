class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i,c in enumerate(expression):
            if c=='{':
                if level==0:
                    start = i+1
                level+=1
            elif c=='}':
                level-=1
                if level==0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            # 只有最内层的','需要计算
            elif c==',' and level==0:
                groups.append([])
            elif level==0:
                groups[-1].append([c])
                print(c,groups)
        resSet = set()    
        for group in groups:
            resSet |= set(map(''.join,itertools.product(*group))) # 求笛卡尔积
        return sorted(resSet)