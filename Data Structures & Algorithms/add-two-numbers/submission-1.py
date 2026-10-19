class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1v = ""
        l2v = ""

        while l1:
            l1v += str(l1.val)
            l1 = l1.next

        while l2:
            l2v += str(l2.val)
            l2 = l2.next

        result = str(int(l1v[::-1]) + int(l2v[::-1]))

        dummy = ListNode(0)
        current = dummy

        for digit in result[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next