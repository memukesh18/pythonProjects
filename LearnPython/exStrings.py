#!/usr/bin/python


print("Hello there!\nHow are you?\nI\'m doing fine.")
print()

print('------------Raw Strings------------')
print(r"Hello there!\nHow are you?\nI\'m doing fine.")

print()
print('------------Multiline print----------')
print()
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.


sincerely,
Bob''')


print('-----------String Methods--------------')

spam = 'Hello World!'
spam = spam.lower()
print(spam)

spam = spam.upper()
print(spam)

print(spam.isupper())
print(spam.islower())

checkAlpha = 'hello'.isalpha()
print('Alpha \t\t : ', checkAlpha)

checkAlNum = 'hello1234'.isalnum()
print('alpha-num \t : ', checkAlNum)

checkDecimal = '1233'.isdecimal()
print('Decimal \t : ', checkDecimal)

checkSpace = '     '.isspace()
print('Spaces or tabs \t : ', checkSpace)

checkTitle = 'This Is A Title Case Example.'.istitle()
print('Title Case \t : ', checkTitle)

checkTitle = 'This Is not a Title case example.'.istitle()
print('Not Title case \t : ', checkTitle)
print()

starts = 'Hello world!'.startswith('Hello')
print('"Hello world!" starts with "Hello": ', starts)

ends = 'Hello world!'.endswith('world!')
print('"Hello world!" ends with "world!": ', ends)



