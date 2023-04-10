def say_hello(user_name ="anonymous"):
    print("hello", user_name)

say_hello('gon')
say_hello()


def tax_calc(money):
    return money * 0.35

tax = tax_calc(123)
    
def pay_tax(tax):
    print('thank you for paying', tax)
    
pay_tax(tax)

pay_tax(tax_calc(1000));




