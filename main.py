#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:59:13 2022

@author: Martin Holguin
"""

import threading
import extract
import process
import display
import q


def play():

    oldBucket = q.Queue()
    newBucket = q.Queue()

    extract_thread = threading.Thread(target=extract.extract_frames, args=(oldBucket, ))
    con_grayscale_thread = threading.Thread(target=process.con_grayscale, args=(oldBucket, newBucket))
    display_thread = threading.Thread(target=display.display, args=(newBucket, ))

    extract_thread.start()
    con_grayscale_thread.start()
    display_thread.start()


if __name__ == '__main__':
    play()
