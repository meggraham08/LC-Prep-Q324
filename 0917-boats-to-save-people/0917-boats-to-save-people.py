class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # [ 1, 2] limit = 3
        #   l , r    r + l == limit
        # 
        #. [ 3, 2, 2, 1]
        #  [ 1, 2, 2, 3]
        #       l/r  count 3

        # [ 3, 3, 4, 5]
        #   l        r

        # Insights
        # if largest number 
        boat = 0
        people.sort()
        left = 0 
        right = len(people) - 1
        while left <= right:
                boat += 1
                if people[left] + people[right] <= limit:
                    left += 1
                right -= 1
        return boat