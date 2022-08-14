from common import *

def reverse_sub_list_own(head, p, q):

    i = 1
    curr = head
    prev = None
    prev_before_p = None
    p_node = None
    while i != p:
        prev_before_p = curr
        curr = head.next
        i += 1
    
    p_node = prev_before_p.next 
    after_q_node = None

    while i != q + 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

        after_q_node = curr
        i += 1

    prev_before_p.next = prev
    p_node.next = after_q_node
    # print_ll(prev)
    return head

def reverse_sub_list(head, p, q):
    if p == q: 
        return head
    
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    #once it exits the while loop, i is at (p-1), for example p is 2, p -1 = 1, 
    # i will be equal to 1, current is pointing to first element

    last_node_of_first_part = previous
    last_node_of_sub_list = current
    next = None

    i = 0
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
    
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous
    else:  # this means p == 1
        head = previous
    
    last_node_of_sub_list.next = current
    return head
    
hello = list_maker([1,2,3,4,5,6])
# print_ll(hello)

print_ll(reverse_sub_list(hello, 2, 6))