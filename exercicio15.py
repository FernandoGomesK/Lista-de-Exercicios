from random import randint

surprise = randint(1, 100)

def guesses():
    while True:
        try:
            guess = int(input("Chute um número: "))
            if guess == surprise:
                print("você acertou!")
                return surprise
            elif guess > surprise:
                print("tente um número menor")
            else:
                print("tente um número maior")            
        except ValueError:
            print("número inválido")
    
guesses()