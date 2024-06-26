class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def mergeLists(lists):


    if not lists or len(lists) == 0:
        return None # if there is na empty list

    while len(lists) > 1: # keep merging till there is only one list left

        mergedLists = []


        for i in range(0, len(lists), 2): # incrementing by 2 since we taking pairs
            l1 = lists[i]
            l2 = lists[i+1] if (i + 1) < len(lists) else None
            mergedLists.append(merge(l1, l2))

        lists = mergedLists
        return lists[0]

        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next

                else:
                    tail.next = l1
                    l1 = l1.next

                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2

            return dummy.next
