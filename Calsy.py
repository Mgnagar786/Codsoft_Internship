# Design a simple calculator with basic arithmetic operations.
print('''
+ Add
- Subtract
* Multiply
/ Divide
''')
num1=int(input('Enter the value1:-'))
num2=int(input('Enter the value2:-'))
operator=input("+,-,*,/")
# Now Follow The Command
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("invalid operator")
