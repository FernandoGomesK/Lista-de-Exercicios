
def checker(a, b):
    refence1 = sorted(list(a))
    refence2 = sorted(list(b))
    if refence1 == refence2:
        print("essa palavra é um anagrama")
    else:
        print('essa palavra não é um anagrama')

word1 = input("digite a primeira palavra: ").strip().lower()
word2 = input("digite a segunda palavra: ").strip().lower()

checker(word1, word2)