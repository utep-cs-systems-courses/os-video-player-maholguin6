#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:57:10 2022

@author: Martin Holguin
"""



import cv2

# globals
frameDelay = 42  # the answer to everything


def display(bucket):
    count = 0
    while bucket.size() != 0:
        print(f'Displaying frame {count}')
        # Read the next frame file
        g_frame = bucket.dequeue()

        # Display the frame in a window called "Video"
        cv2.imshow('Video', g_frame)

        # Wait for 42 ms and check if the user wants to quit
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break

        count += 1

    # make sure we clean up the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()