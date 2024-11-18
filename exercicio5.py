def tabu(x):
    for i in range(11):
      result = x * i
      print(f"a tabuada do número é: {result}")
    return x


def check():
    while True:
        try:
            num1 = input("digite um número para saber sua tabuada: ")
            num1 = int(num1)
            return num1
        except ValueError:
            print("número inválido")
            
number_multi = check()
tabu(number_multi)