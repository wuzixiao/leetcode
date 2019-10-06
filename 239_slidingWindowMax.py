from typing import List
from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        pq = nums[:k]
        #heapq.heapify(pq) # no need to use and it becomes faster
        ret = [heapq.nlargest(1,pq)[0]]  # maxheap
        for i in range(len(nums) - k) :
            pq.remove(nums[i])
            pq.append(nums[i+k])
            #heapq.heapify(pq)
            ret.append(heapq.nlargest(1, pq)[0])

        return ret

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        ret = []
        if not nums:
            return ret

        dq = deque([0])  # use deque to save the index of nums
        for i in range(1,k):
            j = len(dq)
            while j > 0 and nums[i] > nums[dq[j-1]]: # remove the small items before new item
                dq.remove(dq[j-1])
                j = j - 1
            dq.append(i)

        ret.append(nums[dq[0]]) #most left is always biggest item

        for i in range(k, len(nums)):
            if dq[0] == i - k:
                dq.popleft()  # pop out most left item if it's in deque
            j = len(dq)
            while j > 0 and nums[i] > nums[dq[j-1]]:
                dq.remove(dq[j-1])
                j = j -1
            dq.append(i)

            ret.append(nums[dq[0]]) #most left is always biggest item

        return ret

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        window, ret = [], []
        for i, v in enumerate(nums):
            if i >= k and window[0] <= i-k:
                window.pop(0)
            while window and v >= nums[window[-1]]:
                window.pop()
            window.append(i)
            
            if i >= k -1 :
                ret.append(nums[window[0]])
        
        return ret

s = Solution()
ret = s.maxSlidingWindow([3,1,-3,5,4,5],3)
ret2 = s.maxSlidingWindow2([3,1,-3,5,4,5],3)
ret3 = s.maxSlidingWindow3([3,1,-3,5,4,5],3)
ret4 = s.maxSlidingWindow3([1,-1],1)

print(ret2)
print(ret3)
print(ret4)
