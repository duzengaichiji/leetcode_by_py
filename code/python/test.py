class Heap:
    # 最小堆
    def __init__(self,nums):
        self.nums = nums
        self.length = len(nums)
    def buildHeap(self):
        """
        建堆过程
        :return:
        """
        for i in range(self.length//2,-1,-1):
           self.tune(i)
    def popHead(self):
        """
        弹出堆顶元素
        :return:
        """
        popd = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums = self.nums[:-1]
        self.tune(0)
        return popd
    def tune(self,index):
        """
        自上而下调整
        :return:
        """
        arr = self.nums
        while index<self.length:
            left = index*2+1
            right = index*2+2
            if left<self.length and right<self.length:
                if arr[left]<arr[right]:
                    if arr[index]>arr[left]:
                        arr[index],arr[left] = arr[left],arr[index]
                    index = left
                else:
                    if arr[index]>arr[right]:
                        arr[index],arr[right] = arr[right],arr[index]
                    index = right
            elif left<self.length:
                if arr[index] > arr[left]:
                    arr[index], arr[left] = arr[left], arr[index]
                index = left
            elif right<self.length:
                if arr[index] > arr[right]:
                    arr[index], arr[right] = arr[right], arr[index]
                index = right
            else:
                break

if __name__ == '__main__':
    a = [1,7,4,6,4,5,3,10]
    heap = Heap(a)
    heap.buildHeap()
    print(heap.nums)
    heap.popHead()
    print(heap.nums)