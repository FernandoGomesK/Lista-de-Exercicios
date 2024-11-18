text = 'Little pigs, little pigs let me in!'

words = text.lower().split()

def repeater(y):
    repeated_counter = 0
    for x in y:
        if x == x in y:
            repeated_counter+=1
    print(repeated_counter)
            
repeater(words)