#!/usr/bin/python3
"""
function that checks if all boxes can be unlocked
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