#!/usr/bin/python3

nums = range(0,10)

# print all even numbers
print([num for num in nums if num % 2 == 0])

#print an exponentiation of even numbers:
print([num ** 2 for num in nums if num % 2 == 0])

#Add the even numbers to a list called even_primes-
#notes that each number is converted to a string:

even_primes = []
[
    even_primes.append(
        str(num ** 2)
    ) for num in nums if num % 2 == 0
]

print(', '.join(even_primes))

print([(num, num * 2, num ** 2) for num in nums])




