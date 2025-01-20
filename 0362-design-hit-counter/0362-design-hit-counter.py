class HitCounter:
    def __init__(self):
        self.hits = [0] * 300  # Fixed-size array for counts
        self.timestamps = [0] * 300  # Fixed-size array for timestamps

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300  # Map the timestamp to a bucket
        if self.timestamps[index] != timestamp:
            # Reset the bucket if it's for an older timestamp
            self.timestamps[index] = timestamp
            self.hits[index] = 1
        else:
            # Increment the count in the current bucket
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            # Only count hits within the 5-minute window
            if timestamp - self.timestamps[i] < 300:
                total += self.hits[i]
        return total

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)