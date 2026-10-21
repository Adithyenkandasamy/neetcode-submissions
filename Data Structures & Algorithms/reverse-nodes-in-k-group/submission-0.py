class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Step 1: Find the kth node
            group_end = group_prev

            for _ in range(k):
                group_end = group_end.next

                if not group_end:
                    return dummy.next

            # Step 2: Save the next group
            group_next = group_end.next

            # Step 3: Reverse the current group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Step 4: Connect the reversed group
            group_start = group_prev.next
            group_prev.next = group_end
            group_prev = group_start