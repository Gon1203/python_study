def print_hello():
    print('hello world')
    return

print_hello()

message = ''

def set_message(input):
    message = input;
    return message

print('result = ',set_message('hello world'))
print(message)

def set_name_age(name , age):
    # return [name , age]
    return {'name':name, 'age':age}

print(set_name_age("gon", 12))

def set_default_value(temp = 'temp'):
    print(temp)
    return

set_default_value();
set_default_value('value')

class calculator:
    def plus(a = 0,b = 0):
        print(a+b)
    def minus(a = 0,b = 0):
        print(a - b)
    def multiple(a = 0, b = 0):
        print(a * b)

calculator.multiple(1,2)
