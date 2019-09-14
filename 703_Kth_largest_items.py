import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = nums
        heapq.heapify(self._nums)
        
        while len(self._nums) > k:
            heapq.heappop(self._nums)
        

    def add(self, val: int) -> int:
        if len(self._nums) < self._k :
            heapq.heappush(self._nums,val)
        #elif val > heapq.nsmallest(1,self._nums)[0] : it works but slow
        elif val > self._nums[0]:
            heapq.heappushpop(self._nums,val)
        
        return self._nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)