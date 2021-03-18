# **Calculator** - A simple calculator to do basic operators {+-/*^}. 

def oper(a,op,b):
    if op == "+":
        return (f"({str(a)} {op} {str(b)} = {str(a+b)})")
    elif op == "-":
        return (f"({str(a)} {op} {str(b)} = {str(a-b)})")
    elif op == "/":
        return (f"({str(a)} {op} {str(b)} = {str(a/b)})")
    elif op == "*":
        return (f"({str(a)} {op} {str(b)} = {str(a*b)})")
    elif op == "^":
        return (f"({str(a)} {op} {str(b)} = {str(a**b)})")

    else:
        return "Invalid operator"

def calc():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    o = input("Operator: ")

    print(oper(x,o,y))

if __name__ == "__main__":
    calc()
