import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [ -cnt for cnt in count.values()] #highest value at top

        heapq.heapify(maxHeap) 

        time = 0 

        queue = deque() #queue will hold the time value in its length
 
        cooling = 0
        while maxHeap or cooling: 
            if maxHeap:
                queue.extend([0] * (n - len(queue))) #ensure queue is propper size
                cnt = heapq.heappop(maxHeap) + 1
                queue.append(cnt) #frequency (neg -> 0) (appending 0's)
                if cnt: 
                    cooling += 1
            
            if queue: 
                val = queue.popleft()
                if val:
                    cooling -= 1
                    heapq.heappush(maxHeap, val) #add it to heap if not None
                
            time += 1

                


        return time



