#!/usr/bin/python

# function without parameter
def example():
    print('this is basic function..')
    z = 3 + 5
    print(z)
    
example()


#function having parameter
def simpleAddtion(num1, num2):
    res = num1 + num2
    print('num1 is ', num1)
    print(res)
    
simpleAddtion(5, 3)
simpleAddtion(num2=6, num1=4)

#function with default parameteres

def defaultFunc(num1, num2=5):
    print('this is default function block.')
    result = num1 + num2
    print(result)
    print('\n')
    

defaultFunc(3)




def greet(name):
    """
    This function greets to the Person 
    passed into the name parameter.
    """
    print('Hello, '+ name +'. Good Morning!')
    
greet('Paul')
print(greet.__doc__)
