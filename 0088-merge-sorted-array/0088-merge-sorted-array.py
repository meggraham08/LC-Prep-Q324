class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. loop over nums one and have a pointer point lat right most side
        # 2. stick another pointer at nums 2 at right most side
        # 3. look for largest number with another pointer within nums1
        # 4. check if num at pointer 1 is larger than nums2 pointer and vice versa
        # 5. largest between the two goes at nums1 0 pointed pointer and replacs that number
        # 6. move nums2 if that was used, or nums1 to the left 
        #  and then nums1 pointer to left for the next 0 place and then do 3.-6 again until we are at the left most side of both
        last = m + n - 1 # size of nums1+nums2 - 1  we are staring at right most part of the array

        while m > 0 and n > 0: # while we arent at the start of either arrays
            if nums1[m-1] > nums2[n-1]: # if ele for nums1 at the end is larger than nums2 end ele
                nums1[last] = nums1[m- 1] #ovewrite the 0s place with the largest nums1 element
                #update pointer by moving to the left
                m -= 1
            else: # otherwise, ele for nums2 is larger than or equal to nums1s ele
                # equal or nums 2 is greater
                nums1[last] = nums2[n-1] # we shall set this larger num to where the last now is 
                n -= 1 # again we move this pointer and move it to the lft since we are starting at right
                
            last -= 1 # either way, once weve overwritten the zero to the largest number, we need to move the last pointer to the left
        # fill nums1 with leftover nums2 element
        while n > 0 : # since we know n is smaller or equal to m
       # This loop runs if n > 0, meaning there are still elements
       # left in nums2 that haven't been copied to nums1. This happens when all elements of nums1 
       #have already been placed in their correct positions, but some elements from nums2 are still unprocessed.
            nums1[last] = nums2[n - 1] # place leftover nums2 elements in nums1
            n -= 1 # moving the pointers left
            last -= 1
           
