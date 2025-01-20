import logo
print(logo.cal)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operation={
    "+": add,
    "-": sub,
    "*": mul,
    "/":div
}
check =True
while(check):
    first=int(input("Enter First Number: "))
    """
    Add -> +
    Sub -> -
    Mul -> *
    Div -> /
    """
    for symbol in operation:
        print(symbol)
    choice=str(input("What You Want? "))
    sec=int(input("Second Number: "))
    if(choice=='+'):
        print(f"Sum is {add(first,sec)}")
    elif(choice=='-'):
        print(f"Sub is {sub(first,sec)}")
    elif(choice=='*'):
        print(f"Mul is {mul(first,sec)}")
    elif(choice=='/'):
        print(f"Div is {div(first,sec)}")
    c=str(input("Enter 'Y' to Calculate new number")).lower()
    if(c!='y'):
        check=False

