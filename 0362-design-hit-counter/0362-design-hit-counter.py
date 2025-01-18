from collections import deque
from threading import Lock
class HitCounter:
    def __init__(self):
        self.hits = deque()  # Store (timestamp, count) pairs
        self.lock = Lock()   # For thread safety
        
        

    def hit(self, timestamp: int) -> None:
        with self.lock:
            self.hits.append(timestamp)
            # Remove hits older than 5 minutes (300 seconds)
            while self.hits and self.hits[0] <= timestamp - 300:
                self.hits.popleft()

    def getHits(self, timestamp: int) -> int:
        with self.lock:
            # Remove expired hits
            while self.hits and self.hits[0] <= timestamp - 300:
                self.hits.popleft()
            return len(self.hits)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)