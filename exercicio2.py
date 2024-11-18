def even_check(x):
    if x % 2 == 0:
        print("este número é par")
    else:
        print("este número é impar")

def checknum(): 
    while True:
        try:
            num_forcheck = int(input("digite um número para saber se é par: "))
            return num_forcheck
        except ValueError:
            print("este número é inválido")

num1 = checknum()

even_check(num1)