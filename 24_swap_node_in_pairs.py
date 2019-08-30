# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    def swapPairs(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None) :
            return head

        ret = head.next
        cur = head
        pre = None
        
        while(cur!=None and cur.next!=None) :

            nextTmp = cur.next
            cur.next = nextTmp.next # 2->3->4  1->3->4
           # cur.next.next = cur  # 2->1->3->4
            nextTmp.next = cur

            if(pre != None) :
                pre.next = nextTmp

            cur = cur.next
            pre = nextTmp.next
        
        return ret
    

sol = Solution()
sol.swapPairs(sol.n1)


