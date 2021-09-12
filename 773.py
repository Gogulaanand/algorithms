https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/773/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        x = set()
        while head and head.next is not None:
            if head in x:
                return True
            else:
                x.add(head)
                head = head.next
        return False


# Algorithm: https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
# python concept: 
  # better ask for forgiveness than permission
  # https://docs.python.org/3/glossary.html#term-eafp
  # https://docs.python.org/3/glossary.html#term-lbyl


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow!=fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False