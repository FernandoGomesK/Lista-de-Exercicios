def check1():
    while True:
        try:
            num1 = input("Primeira nota para a média: ")
            num1 = int(num1)
            return(num1)
        except ValueError:
            print('número inválido!')
def check2():
    while True:
        try:
            num2 = input("segunda nota para a média: ")
            num2 = int(num2)
            return(num2)
        except ValueError:
            print('número inválido!')
def check3():
    while True:
        try:
            num3 = input("terceira nota para a média: ")
            num3 = int(num3)
            return(num3)
        except ValueError:
            print('número inválido!')
            
def calculate(a, b, c):
    average = (a + b + c) / 3
    if average < a:
        print(f"a nota 1 é maior que a média")
    if average < b:
        print(f"a nota 2 é maior que a média")
    if average < c:
        print(f"a nota 3 é maior que a média")
    else:
        print("")
    return average
    
    
            
num1 = check1()
num2 = check2()
num3 = check3()
result = calculate(num1, num2, num3)
print(result)