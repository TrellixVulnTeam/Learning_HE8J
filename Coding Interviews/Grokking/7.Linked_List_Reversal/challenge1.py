def reverse_sub_list(head, k):
    if k<=1 or head is None: 
        return head
    
    current, previous = head, None

    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        next = None
        i = 0

        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:  
            head = previous
        
        last_node_of_sub_list.next = current
        
        #skip k nodes
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1
        
        if current is None:
            break
        
    return head