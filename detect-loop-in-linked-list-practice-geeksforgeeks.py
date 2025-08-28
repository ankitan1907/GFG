class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        _set = set()
        detact = False
        while head:
            if head not in _set:
                _set.add(head)
                head = head.next
            else:
                detact = True
                break
        return detact