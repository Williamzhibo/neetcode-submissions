class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed)) #creates tuples ordering. 
        cars.sort(key = lambda x: -x[0]) #sorted in decending order
        count = 0 #number of fleets
        prevTime = 0
        for p, s in cars:
            time = (target - p) / s
            if prevTime < time:
                count += 1
                prevTime = time
        return count