> LCS(最长公共子序列)和LIS(最长递增子序列)这两个问题在一定的条件下可以将LCS转换为LIS；
> 
> 通常的LCS解法是O(n²)的复杂度，而LIS可以达到O(nlogn)的复杂度；
> 
> 比如要求 target,arr两个数组的最长公共子序列；
>
> 假如target中的数字**互不相同**；
> 
> 那么我们将arr中的数字在target中的idx进行一个获取，如果不存在，直接剔除；
> 
> 得到数组 pos；即将arr中的数按照在target中的位置重新标号；
> 
> 那么一个**顺序相同**的子序列，就等于**重新标号**后的一个**上升子序列**；
> 
> 因此此时求pos的最长上升子序列，就是求target和arr的最长公共子序列；（参考1713的代码）；