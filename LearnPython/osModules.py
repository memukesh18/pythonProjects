#!/usr/bin/python


import os
import time

curDir = os.getcwd()
print(curDir)


os.mkdir('newDir')

time.sleep(5)

os.rename('newDir', 'newDir2')

time.sleep(2)

os.rmdir('newDir2')


