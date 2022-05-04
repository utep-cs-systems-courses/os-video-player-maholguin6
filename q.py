#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:49:12 2022

@author: Martin Holguin
"""

import threading

QUANTITY = 10


class Queue:

    def __init__(self):
        self.queue = []
        self.status = False

        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(QUANTITY)

    def enqueue(self, resource):
        self.empty.acquire()
        self.lock.acquire()
        self.queue.append(resource)
        self.lock.release()
        self.full.release()

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        resource = self.queue.pop(0)
        self.lock.release()
        self.empty.release()
        return resource
    
    def size(self):
        return len(self.queue)