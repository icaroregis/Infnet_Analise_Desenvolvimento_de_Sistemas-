n = int(input("Digite um número(o mesmo representará o intervalo a ser da soma dos números ímpares): "));

def soma_impares(n):
    somaImpares = 0;
    cont = 0;
    for cont in range(1, n+1, 2):
        somaImpares += cont;
        cont = cont + 1;
    return somaImpares


print(soma_impares(n));