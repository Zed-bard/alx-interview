#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Determines if all boxes can be unlocked.

    Each box may contain keys to other boxes. This function checks if it is
    possible to unlock all the boxes, starting from the first box (box 0).

    Args:
        boxes (list of list of int): A list where each index represents a box 
                                     and each element is a list of keys 
                                     contained in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    n = len(boxes)
    if n == 0:
        return True  # No boxes to unlock

    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx >= n or boxIdx < 0:
            continue  # Skip invalid indices
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)
