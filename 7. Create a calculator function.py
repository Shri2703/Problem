#Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer

#Solution

def perform_operation(num1,operator,num2):
    if operator =="+":
        result = num1+num2
    elif operator =="-":
        result = num1 -num2
    elif operator =="*":
        result = num1*num2
    elif operator =="/":
        if num2!=0: 
            result = num1/num2
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")


    return result        

try:
    num1=int(input("Enter the first integer:"))
    operator =input ("Enter the operator(+,-,*,/): ")
    num2= int(input("Enter the second integer: "))

    result=perform_operation(num1,operator,num2)
    print("Result: ",result)
except ValueError as e:
    print("Error:" ,e)    