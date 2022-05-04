#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:53:09 2022

@author: Martin Holguin
"""

#!/usr/bin/env python3

import cv2

clipFileName = '../clip.mp4'

# open the video clip
vid_cap = cv2.VideoCapture(clipFileName)


def extract_frames(bucket):
    count = 0
    success, image = vid_cap.read()

    while success:
        print(f'Reading frame {count}')
        bucket.enqueue(image)
        success, image = vid_cap.read()
        count += 1
    bucket.status()