# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        curr = head

        while curr:
            if curr.val in visited:
                return True
            visited[curr.val] = curr.next
            curr = curr.next
        return False
