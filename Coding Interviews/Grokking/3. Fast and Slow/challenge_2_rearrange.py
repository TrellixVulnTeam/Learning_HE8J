def reorder(head):
    
    if head is None or head.next is None:
        return
    
    #find middle of the linkedlist
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    #once this loop quits, slow is the middle

    head_second_half = reverse(slow)
    head_first_half = head

    #rearrange to produce linkedlist in the required order
    while head_first_half is not None and head_scond_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp 

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    #set the next of the last node to None
    if head_first_half is not None:
        head_first_half.next = None

def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next 
    return prev

