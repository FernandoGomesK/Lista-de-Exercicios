def checking1():
    while True:
        try:
            num1 = int(input("Digite o primeiro número para a soma: "))
            return num1
        except ValueError:
            print("Esse número é inválido")
            
def checking2():   
    while True:
        try:
            num2 = int(input("Digite o segundo número para a soma: "))
            return num2
        except ValueError:
            print("Esse número é inválido")
            
def sum(a, b):
    if a is not None and b is not None:
        return a + b           

num1 = checking1()
num2 = checking2()

result = sum(num1, num2)           
print(f"O resultado é {result}")
