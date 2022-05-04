#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:55:33 2022

@author: Martin Holguin
"""

#!/usr/bin/env python3

import cv2


def con_grayscale(oldBucket, newBuket):
    count = 0

    while oldBucket.size() != 0:
        print(f'Converting frame {count}')
        extracted_frame = oldBucket.dequeue()
        grayscale_frame = cv2.cvtColor(extracted_frame, cv2.COLOR_BGR2GRAY)
        newBuket.enqueue(grayscale_frame)
        count += 1
