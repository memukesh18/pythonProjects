import time

total = 0
start = time.time()
for num in range(101):
    total = total + num
print(total)
print("The entire Job took ", time.time()-start)


totalSum = 0
n = 100
start = time.time()
totalSum = (n * (n+1))/2
print(totalSum)
print("The entire Job took ", time.time()-start)



