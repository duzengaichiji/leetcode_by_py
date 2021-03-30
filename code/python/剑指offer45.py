class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort(l,r):
            #print(nums)
            if l>=r:return
            i,j = l,r
            inc = nums[l]
            while i<j:
                while i<j and compare(nums[j],inc,0,0)==True:
                    j-=1
                if i<j:
                    nums[i] = nums[j]
                    i+=1
                while i<j and compare(inc,nums[i],0,0)==True:
                    i+=1
                if i<j:
                    nums[j] = nums[i]
                    j-=1
            nums[j] = inc
            if j-l>1:
                sort(l,j-1)
            if r-j>1:
                sort(j+1,r)
            return
        def compare(num1,num2,i1,i2):
            if num1==num2:
                return True
            if len(set(num1))==1 and len(set(num2))==1 and num2[0]==num1[0]:
                return True
            if num1[i1]<num2[i2]:
                return False
            elif num1[i1]>num2[i2]:
                return True
            else:
                i1+=1
                i1 = i1%len(num1)
                i2+=1
                i2 = i2%len(num2)
                return compare(num1,num2,i1,i2)
        nums = [str(num) for num in nums]
        sort(0,len(nums)-1)
        return "".join(nums)