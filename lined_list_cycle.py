"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    # if you hop back to a node you already visited, theres a cycle
    visited = set()
    # want to keep track of places we've3 been
    # only go to each place once
    # maybe a visited set?

    # iterate through the linked list
    node = head
    while node.next is not None:
        # if the node isn't in visited, add it ---> store the entire node
        if node in visited:
            # if it is, return True --> there's a cycle
            return True
        else:
            visited.add(node)
        node = node.next
    # if we iterate through the entire linked list, return False
    return False

