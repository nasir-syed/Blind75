
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove(head, n):
    dummy = ListNode(0, head)

    l = dummy
    r = head


    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        l = l.next
        r = r.next

    # delete
    l.next = l.next.next
    return dummy.next

