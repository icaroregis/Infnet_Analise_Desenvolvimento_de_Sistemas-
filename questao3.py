# from math import factorial
# n = int(input("Digite um número para que seja calculado o seu fatorial: "))
# f = factorial(n)
# print("O fatorial de {} é {}".format(n, f));
    
n = int(input("Digite um número para que seja calculado o seu fatorial: "))

def calc_fatorial(n):
    fatorial = 1
    for c in range(1, n+1):
        fatorial = fatorial * c
    return fatorial

print("O fatorial de {} é {}".format(n, calc_fatorial(n)));
        
    
