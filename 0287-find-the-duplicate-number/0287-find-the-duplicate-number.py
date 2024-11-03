class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            print("slow", slow, "fast", fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("fast AGAIN", nums[nums[fast]])
            if slow == fast:
                break
                

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow