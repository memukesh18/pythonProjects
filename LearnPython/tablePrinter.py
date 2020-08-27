#!/usr/bin/python3

"""
# write a program that does following.
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
"""


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

 
def printTable():
    colWidths = [0]*len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))
    
    
    for i in range(len(tableData[i])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()

printTable()



