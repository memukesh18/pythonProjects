varJoin = '!,'.join(['cats','rats','bats'])
print(varJoin)

varSplit = 'I Love to visit beautiful places specially mountains'.split()
print(varSplit)

print()

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labled "Milk Experiment".

Please do not drink it.

Sincerely,
Bob'''

spamlist = spam.split('\n')

print(spamlist)
print()


print('Hello'.rjust(10))
print('Hello'.rjust(10, '*'))

print('Hello'.ljust(10))
print('Hello'.ljust(10, '!'))

print('Hello World'.center(20))
print('Hello World'.center(20, '-'))
print()


spam = '    hello World    '
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())


spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))  #strip func removes any leading and trailing characters
