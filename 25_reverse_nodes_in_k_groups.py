# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         pre = None
#         while(cur != None) :
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre

#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(-1)
#         cur, pre = head, dummy

#         while not cur :
#             last = iter(k, cur)
#             if not last :
#                 next = last.next
#                 last.next = None
#                 start = reverseList(cur)
#                 iter(k, start).next = next
#                 pre.next = start

#                 pre = iter(k, start)
#                 cur = next
#             else : 
#                 pre.next = cur
#                 break

#         return dummy.next

#     def iter(k, start) -> ListNode :
#         count = k
#         cur = start
#         while(count > 1 and not cur) :
#             cur = cur.next
#             count -= 1
        
#         return cur

class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next
