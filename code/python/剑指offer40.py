class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        return arr[:k]