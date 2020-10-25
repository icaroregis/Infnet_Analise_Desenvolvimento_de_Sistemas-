n = int(input("Digite um número(o mesmo representará o intervalo da soma dos números ímpares): "));

def soma_impares(n):
    soma = 0;
    for cont in range(1, n+1):
        if(cont % 2 != 0):
            print(cont, end=" ")
            soma += cont
    return soma

print("A soma dos números ímpares é: {}".format(soma_impares(n), end=" "));