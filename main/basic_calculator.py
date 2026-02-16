#This is a basic calculator

import sys


def get_numbers():
    while True:
        try:
            a = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid, Please try again!")
    while True:
        try: 
            b = float(input("Enter the second number: "))
            return a, b
        except ValueError:
            print("Invalid, Please try again!")
        

def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b):
    while b == 0:
        print("Canno't be divided by zero")
        b = float(input("Enter the second number: ")) 
    return a / b

def confirm_exit():
    while True:
        c = input("Are you sure? (Y/N): ").strip().upper()
        if c == "Y":
            return True
        elif c == "N":
            return False
        else: print("Invalid")


        
ops = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def operator():
    while True:
        op = input("Please choose an operator (+ - * /) or type 'Exit': ").strip().lower()
        if op in ops:
            a, b = get_numbers()
            result = ops[op](a, b)
            print(f"{a} {op} {b} = {result:.2f}")
        elif op == "exit":
            if confirm_exit():
                sys.exit(0)
            continue
        else:
            print("Invalid Operator")
    
def main():
    operator()


if __name__ == '__main__':
    main()