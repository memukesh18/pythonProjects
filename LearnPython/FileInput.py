#!/usr/bin/python

text = 'Hello there this is new file.\nThis is new line.'
apendMe = '\nNew bit of information'

saveFile = open('./Files/newFile.txt', 'w')
saveFile.write(text)
saveFile.close()


apendFile = open('./Files/newFile.txt', 'a')
apendFile.write(apendMe)
apendFile.close()


readMe = open('./Files/newFile.txt', 'r').read()
print(readMe)