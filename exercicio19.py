phrase = input("digite uma frase para a contagem de caractéres: ")

def count(x):
    characters = {
    }
    for y in x:
        if y not in characters:
            characters[y] = 1
        else:
            characters[y] += 1
    return characters

result = count(phrase)
print(result)