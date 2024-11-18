def conversor(x):
    if c is not None:
        print((x * 1.8) + 32)

def check():
    while True:
        try:
            c = float(input("Digite um número para a conversão: "))
            return c
        except ValueError:
            print("Digite um número válido")

c = check()
farenshot = conversor(c)