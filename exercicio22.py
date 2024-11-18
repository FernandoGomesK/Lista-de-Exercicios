vowels = ['a', 'e', 'i', 'o' ,'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def word():
    vowel_count= 0
    consonant_count= 0
    uord = input("digite a palavra para a contagem: ")
    for x in uord:
        if x in vowels:
            vowel_count+=1
        elif x in consonants:
            consonant_count+=1
    print(f'a palavra tem {consonant_count} consoantes')
    print(f'a palavra tem {vowel_count} vogáis')
        

word()