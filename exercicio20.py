fibo = [0, 1]

def the_sequence(i):
    while len(fibo) < i:  
        next_number = fibo[-1] + fibo[-2]
        fibo.append(next_number)
    return fibo

size = the_sequence(20)
print(size)