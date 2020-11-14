class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        stack = []
        count = 0
        for i in num:
            if not stack or count == k:
                stack.append(i)
            else:
                # 维护单调递增栈，保存结果
                while stack and int(i) < int(stack[-1]):
                    stack.pop()
                    count += 1
                    if count == k:
                        break
                stack.append(i)
        # 移除的次数还不够，从栈顶开始继续移除
        while count < k:
            stack.pop()
            count += 1
        res = "".join(stack)
        # 拼接结果
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        res = res[i:]
        if len(res) == 0:
            return '0'
        return res