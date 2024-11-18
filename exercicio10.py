def check1():
    while True:
        try:
            base = input("Digite o tamanho da base: ")
            base = int(base)
            return base
        except ValueError:
            print("Valor inválido!")
            
def check2():
    while True:
        try:
            altura = input("Digite a altura: ")
            altura = int(altura)
            return altura
        except ValueError:
            print("Valor inválido!")
            
def calculum(a, b):
    return (a * b) / 2
            
base = check1()
altura = check2()
result = calculum(base, altura)
print(result)
