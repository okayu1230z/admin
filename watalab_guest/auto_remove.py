#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from operator import itemgetter

DIR_PATH = "data"
MAX_FILE_NUMBER = 30

def auto_remove():
    filelists = []
    for file in os.listdir(DIR_PATH):
        base, ext = os.path.splitext(file)
        if ext == '.zip':
            filelists.append([file, os.path.getctime(DIR_PATH + "/" + file)])
    filelists.sort(key=itemgetter(1), reverse=True)
    for i, file in enumerate(filelists):
        if i > MAX_FILE_NUMBER - 1:
            os.remove(DIR_PATH + "/" + file[0])
    return

if __name__ == "__main__":
    auto_remove()
