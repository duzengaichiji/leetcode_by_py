class Solution {
    public int minArray(int[] numbers) {
        int left = 0;
        int right = numbers.length-1;
        while(left<right){
            int pivot = left+(right-left)/2;
            if(numbers[pivot]<numbers[right]) right = pivot;
            else if(numbers[pivot]>numbers[right]) left = pivot+1;
            else right--;
        }
        return numbers[left];
    }
}