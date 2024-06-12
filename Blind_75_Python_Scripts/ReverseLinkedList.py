# Definition of singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def reverse(head):

    # iterative solution using pointers

    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


    # recursive solution (more memory complexity)

     # if not head:
     #     return None
     #
     # newHead = head
     #
     # if head.next: # if there is another node
     #    self.reverse(head.next)
     #    head.next.next = head
     #    # reversing the link
     #
     # head.next = None
     #
     # return newHead
