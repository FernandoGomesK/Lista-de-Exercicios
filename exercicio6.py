def standart(a, b ,c):
    average = (a + b + c) / 3
    return average

def check1():
    while True:
        try:
           num1 = input("Digite o primeiro número para média: ")
           num1 = int(num1)
           return num1
        except ValueError:
            print("número inválido")
            
def check2():
    while True:
        try:
           num2 = input("Digite o segundo número para média: ")
           num2 = int(num2)
           return num2
        except ValueError:
            print("número inválido")
            
def check3():
    while True:
        try:
           num3 = input("Digite o terceiro número para média: ")
           num3 = int(num3)
           return num3
        except ValueError:
            print("número inválido")
            
num1 = check1()
num2 = check2()
num3 = check3()
result = standart(num1, num2, num3)
print(result)