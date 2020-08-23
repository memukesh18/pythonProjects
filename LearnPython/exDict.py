
birthdays = {'Alice' : 'Apr 1', 'Bob': 'july 5', 'Joy': 'Aug 14'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t have birthdays information for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated!')    
    
    
for k, v in birthdays.items():
    print('key: ' + k + ', Value: ' + str(v))
    

print('\n')

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)
