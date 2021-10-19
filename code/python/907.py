class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        if len_A == 0:
            return 0
        if len_A == 1:
            return A[0]

        ans = 0
        left = [0] * len_A
        right = [0] * len_A

        stack = []
        for i in range(len_A):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(len_A - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                right[i] = len_A
            else:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(len_A):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 1000000007
        return ans