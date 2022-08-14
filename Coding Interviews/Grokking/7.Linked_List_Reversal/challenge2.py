from common import *

def rotate(head, rotations):
    if head is None or head.next is None or rotations <= 0:
        return head

    #find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1
    
    last_node.next = head #connect the last node with the head to make it a circle
    rotations %= list_length
    skip_length = list_length - rotations
    last_node_of_rotated_list = head

    #if length is 6, rotations is 2, skip_length = 4, so range(3)
    for i in range(skip_length -1):
        last_node_of_rotated_list = last_node_of_rotated_list.next
    # 1 2 3 4 5 6 -> 5,6,1,2,3,4, we need to next 3 times

    #now we set head to the last one's next
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    return head
