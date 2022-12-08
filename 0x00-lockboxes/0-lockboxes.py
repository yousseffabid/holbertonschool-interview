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
    """unlock boxes"""
    number_boxes = len(boxes)
    keys = boxes[0]
    box_locked = [False] + [True] * (number_boxes - 1)
    for key in keys:
        if ((key < number_boxes) and (box_locked[key] is True)):
            box_locked[key] = False
            keys.extend(boxes[key])
    return not any(box_locked)