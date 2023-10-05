#function to perform addition 
def add(x,y):
    return x+y

#function to perform subtraction
def subtract(x,y):
    return x-y

#function to perform multiplication
def multiply(x,y):
    return x*y

#function to perform division
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y

#main
while True:
    print("options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    choice=input("Enter operation choice:")
    if choice=='quit':
        break

    if choice in ('add','subtract','multiply','divide'):
        num1=float(input("enter first number"))
        num2=float(input("enter second number"))

        if choice=='add':
            result=add(num1,num2)
        elif choice=='subtract':
            result=subtract(num1,num2)
        elif choice=='multiply':
            result=multiply(num1,num2)
        elif choice=='divide':
            result=divide(num1,num2)

        print(f"Result:{result}\n")
    else:
            print("invalid input. please enter a vaild operation.\n")