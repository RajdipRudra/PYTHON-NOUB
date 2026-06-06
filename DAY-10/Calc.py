from art import logo

print(logo)

def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multi(a,b):
    return a*b
def divition(a,b):
    return a/b


operationss = {
    "+":addition,
    "-":substraction,
    "*":multi,
    "/":divition
}


first_num = int(input("What's the first num?: "))
while True:
    operation = input("+\n-\n*\n/\npick an operation: ")
    sec_num = int(input("what's the next number?: "))
    if operation in operationss:
        output = operationss[operation](first_num,sec_num)
        print(f"{first_num}{operation}{sec_num} = {output}")
    else:
        operation = input("+\n-\n*\n/\npick an operation: ")
        output = operationss[operation](first_num,sec_num)
        print(f"{first_num}{operation}{sec_num} = {output}")
        
    contiNuee = input("do u wanna continue with the output? y or n").lower()
    if contiNuee=="y":
        first_num = output
    else:
        break
