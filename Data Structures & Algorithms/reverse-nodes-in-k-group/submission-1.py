class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            group_end = group_prev

            for _ in range(k):
                group_end = group_end.next

                if not group_end:
                    return dummy.next

            group_next = group_end.next

            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            group_start = group_prev.next
            group_prev.next = group_end
            group_prev = group_start