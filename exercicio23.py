def num1_check():
    while True:
        try:
            num1 = input("Digite o primeiro número para a operação: ")
            num1 = int(num1)
            return num1
        except ValueError:
            print("número inválido")
            
def num2_check():
    while True:
        try:
            num2 = input("Digite o segundo número para a operação: ")
            num2 = int(num2)
            return num2
        except ValueError:
            print("número inválido")
            
            
def operation(a, b):
    while True:
            symbol = input("digite o simbolo para a operação: ")
            if symbol == "+":
                return a + b
            elif symbol == "-":
                return a - b
            elif symbol == '/':
                if b == 0:
                    print(" essa operação é inválida")
                else:
                    return a / b                   
            elif symbol == '*':
                return a * b
            else:
                print("símbolo inválido")
            
num1 = num1_check()
num2 = num2_check()
result = operation(num1, num2)
print(result)
    