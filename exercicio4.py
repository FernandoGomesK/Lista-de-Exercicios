def counter():
    word = input("digite um palavra para a contagem: ")
    word_count = list(word)
    number = len(word_count)
    print(number)
    return number

counter()