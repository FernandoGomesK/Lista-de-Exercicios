word = input("digite uma frase para contagem: ")

def counter(x):
    unique = set(x.split())
    size = (len(unique))
    print(f"A frase tem {size} palavras únicas")
    
counter(word)
    
    