class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def reOrder(head):
    s, f = head, head.next

    # find middle
    while f and f.next: # while fast is not null and has not reached the end of the list
        s = s.next
        f = f.next.next


    # reversing the second half

    second = s.next
    prev = s.next = None # we're splitting it into two different lists

    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merging the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.nextnotep
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
