# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #base case -- something like this
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
            

        # adding list2 into list1 in the correct spots, so our return will be list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            #redirect list1 next pointer to list2 head, 
            #need to save current list1 next pointer before redirecting
            savedNext1 = list1
            #need to pass in list2.next because thats taking on the new whole list (not losing previous nodes)
            list2.next = self.mergeTwoLists(list2.next, savedNext1)
            return list2
            

        