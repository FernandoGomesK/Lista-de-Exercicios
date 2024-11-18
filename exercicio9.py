def check():
    while True:
        try:
            age = input("digite sua idade para ser conferida: ")
            age = int(age)
            return age
        except ValueError:
            print("Idade inválida")
            
def checker(x):
    if x >= 18:
        print("o usúario tem mais de 18 anos")
        return x
    else:
        print("o usuário tem menos de 18 anos")
            
            
age = check()
checker(age)