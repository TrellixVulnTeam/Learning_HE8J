from common import *
# returns the head of the reversed list
def reverse_linked_list(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        
        #updat prev to current
        prev = head
        #update head to the next one
        head = next
    return prev



def is_palindrome(head):
    if head is None or head.next is None:
        return True
    
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next 
    
    #once it quits the loop, it means slow is at the middle already
    second_half_head = reverse_linked_list(slow)
    copy_second_half_head = second_half_head

    while head is not None and second_half_head is not None:
        if head.value != second_half_head.value:
            break

        head = head.next
        second_half_head = second_half_head.next 
    
    reverse_linked_list(copy_second_half_head)

    if head is None or second_half_head is None:
        return True

    return False


a = list_maker([2,4,6,4,2,1])
print(is_palindrome(a))