# SOLVED

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        
        headL1 = l1
        headL2 = l2

        tempVal = 0
        tempResult = ListNode()
        current = tempResult

        while headL1 or headL2 or tempVal:
            valH1 = 0
            valH2 = 0

            if headL1 != None:
                valH1 = headL1.val
                headL1 = headL1.next

            if headL2 != None:
                valH2 = headL2.val
                headL2 = headL2.next

            tempVal = valH1 + valH2 + tempVal
            current.next = ListNode(tempVal % 10)
            tempVal = int(tempVal / 10)
            current = current.next            

        return tempResult.next
        
if __name__ == "__main__":
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]
    # Expected resultt = [8,9,9,9,0,0,0,1]
    
    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))
    l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None))))
    
    result = Solution().addTwoNumbers(l1, l2)

    head = result
    result = []

    while head:
        result.append(head.val)
        head = head.next


    print(result)