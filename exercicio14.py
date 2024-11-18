def palindrome(x):
    if x == "".join(reversed(x)):
        print("Esta palavra é um palíndromo")
    else:
        print("esta palavra não é um palindromo")
        
word = input("Digite uma palavra para conferir se é um palíndromo: ")
palindrome(word)