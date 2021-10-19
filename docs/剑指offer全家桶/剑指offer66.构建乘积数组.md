剑指offer66.构建乘积数组
----------
 - 题目
>给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 - 示例
 ----------
>input: [1,2,3,4,5]

> output: [120,60,40,30,24]
 ----------
 - 代码
 >
>
    class Solution:
        def constructArr(self, a: List[int]) -> List[int]:
            if not a:return []
            pre = [a[0]]
            for num in a[1:-1]:
                pre.append(pre[-1]*num)
            order = [a[-1]]
            for num in a[::-1][1:-1]:
                order.append(order[-1]*num)
            order = order[::-1]
            print(pre,order)
            res = []
            for i in range(len(a)):
                if i==0:
                    res.append(order[0])
                elif i==len(a)-1:
                    res.append(pre[-1])
                else:
                    res.append(pre[i-1]*order[i])
            return res
 ----------
 - 解析
 > 
> 不让使用除法，那就使用乘法；
>
> 显然，要求除了某个x(i)之外的所有数字的乘积；
>
> 是这样 res = x0*x1*...x(i-1)*...x(n);
>
> 那么，只要有 x0*x1*...x(i-1)以及  x(i+1)*...*x(n)即可；
>
> 因此，创建两个数字pre和order，分别用来记录 **前向累乘** 和 **后向累成**；
>
> 即 对于i位置的res，可以由于pre[i-1]和order[i]获得；
>
> 因为pre[i-1]是i前面的前i-1项乘积，order[i]是i后面的所有数字的乘积;
>
> 