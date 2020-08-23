#!/usr/bin/python

x = [5,6,7,3,5,6,2,6,7,3,6,7]

x.append(4)
x.insert(2,9)		#insert 9 at 2nd index (index starts at 0)
x.remove(2)

print(x)
print("displaying 5 to 8 elements: ", str(x[5:9])) 		#display 5th to (9-1)th index element
print("displaying the index of first 6: ", str(x.index(6)))
print("displaying the last element: ", str(x[-1]))
print()

x.sort()			#sort the list
print(x)

print()


x = [[5,6],[5,9],[4,8],[3,7]]
y = [[[4,6],[3,5]],[[3,2],[4,7]],[[3,5],[4,9]]]

print(x)
print("Elements at x[2][1] : ", str(x[2][1]))
print()
print(y)
print("Elements at y[0][0][1] : ", str(y[0][0][1]))

print()

spam = [2, 4, 6, 8, 10]
x = spam[int(int('3' * 2) // 11)]
print(x)
print(spam[-1])
print(spam[:2])


bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat'))
