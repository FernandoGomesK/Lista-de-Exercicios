def interval():
    inter1 = int(input("digite o início do intervalo: "))
    inter2 = int(input("digite o final do intervalo: "))
    return range(inter1, inter2 + 1)
    


def prime_checker(x):
    if x < 2:
        return False
    for y in range(2, int(x**0.5) + 1):
        if x % y == 0:
            return False
    return True

def prime_counter(inter):
    optimous = []
    for x in inter:
        if prime_checker(x):
            optimous.append(x)
    return optimous
    
    
inter = interval()
primes =  prime_counter(inter)
print(f"estes são os números primos no intervalo {primes}")