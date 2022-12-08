#!/usr/bin/python3

"""
function that checks if all boxes can be unlocked
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""
def canUnlockAll(boxes):
    size = len(boxes)
    
    if not size or not len(boxes[0]):
        return False
    
    
    keys = set(boxes[0])
    
    number_opened_boxes = 1
    
    for i in range(1, size):
        if i not in keys:
            return False

        number_opened_boxes += 1
        
        size_sublist = len(boxes[i])
        
        if size_sublist:
            sublist = boxes[i]
            
        for j in range(size_sublist):
            if sublist[j] <= size - 1 and sublist[j] > 0:
                keys.add(sublist[j])

        if number_opened_boxes == size:
            return True

    return False

