class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m = 0

        n = 0
        res = []
        # nums1 = [1,1,2,2]
        #          ^  
        # nums2 = [2,2]
        while m <= len(nums1)-1 and n <= len(nums2)-1: # while  0 <= 3 and 0 <= 1
            if nums1[m] < nums2[n]:
                m += 1
            elif nums2[n] < nums1[m]:
                n += 1
            elif nums1[m] == nums2[n]:
                res.append(nums1[m])
                m += 1
                n += 1
        return res
            
                



