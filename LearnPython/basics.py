#!/usr/bin/python

#this is single line comment section


'''
This is 
multiline 
comment
section

'''

# if-else conditions

def maxValue(a, b, c):
    if((a >= b) and (c < b)): return a
    elif (a >= b):  return maxValue(a, c, b)
    else: return maxValue(b, a, c)

        
maxVal = maxValue(4, 40, 55)
print("Max Value: ", str(maxVal))


# while loop

condition = 1

while condition < 10:
    print(condition, end=" ")
    condition += 1
print();


# foreach loop in python
exampleList = [1,5,6,1,4,5,63,54,6,5]

for eachItem in exampleList:
    print(eachItem, end= " ")
print('continue..')



for x in range(1,11):
    print(x, end=" ")
print()



# Accepting input from user
x = input('please enter your name\n')
print('hello ', x)

