import threading

class HitCounter:
    def __init__(self):
        self.hits = [0] * 300  # Fixed-size array for counts
        self.timestamps = [0] * 300  # Fixed-size array for timestamps
        self.lock = threading.Lock()  # Lock for thread safety

    def hit(self, timestamp: int) -> None:
        with self.lock:  # Ensure exclusive access
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
        with self.lock:  # Ensure exclusive access
            for i in range(300):
                # Only count hits within the 5-minute window
                if timestamp - self.timestamps[i] < 300:
                    total += self.hits[i]
        return total