class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # arr = [3,2,1,4].  k is the first value in the list
        # return array of k vals corresponding to a sequence
        # it must sort the array
        # pancake flip -- reverse a prefix of the list
        # 1. get largest int in the array and the first element off arr to where largest was
        # [4,2,3,1]
        # perform another flip
        # [1,3,2,4]
        def flip(end):
            start = 0
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        res = []
        k = len(arr)
        for i in range(k-1,-1,-1):
            max_ = i
            for j in range(i,-1,-1):
                if arr[j] > arr[max_]:
                    max_ = j
            if max_ != i:
                flip(max_)
                flip(i)
                res.append(max_+1)
                res.append(i+1)
        return res
        