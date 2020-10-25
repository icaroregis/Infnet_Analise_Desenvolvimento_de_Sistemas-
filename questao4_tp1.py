n = int(input("Digite um número para que seja calculado o seu fatorial: "))

def calc_fatorial(n):
    fatorial = 1
    c = 0
    while(c < n+1):
        fatorial = fatorial * c
        c += 1
    return fatorial

print("O fatorial de {} é {}".format(n, calc_fatorial(n)));