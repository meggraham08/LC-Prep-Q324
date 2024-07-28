class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = 0
        cur_penalty = 0
        earliest_hour = 0

        for i in range(len(customers)):
            ch = customers[i]
            print(ch)
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penalty by 1.
            if ch == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1

            # Update earliestHour if a smaller penalty is encountered.
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty

        return earliest_hour