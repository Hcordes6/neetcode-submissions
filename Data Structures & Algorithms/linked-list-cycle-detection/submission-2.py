# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()

        if not head:
            return False

        while head.next is not None:
            if head not in nodes:
                nodes.add(head)
                head = head.next
            else:
                return True
        return False



        