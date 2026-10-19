# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def splitList(head):
            if head is None or head.next is None:
                return head, None

            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next
            slow.next = None

            return head, second_half

        def reverse(head):
            nextnode = None
            current = head
            prev = None
            while current:
                nextnode = current.next
                current.next = prev
                prev = current
                current = nextnode
            return prev
        def mergeAlternately(list1, list2):
            if not list1:
                return list2

            if not list2:
                return list1

            head = list1

            while list1 and list2:
                next1 = list1.next
                next2 = list2.next

                list1.next = list2

                if next1:
                    list2.next = next1
                list1 = next1
                list2 = next2
            return head    
        if head is None or head.next is None:
            return 
        current = head
        list1,list2 = splitList(current)
        rev = reverse(list2)
        mergeAlternately(list1,rev)