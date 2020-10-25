a = float(input("Digite o 1º segmento: "));
b = float(input("Digite o 2º segmento: "));
c = float(input("Digite o 3º segmento: "));

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo', end='')
    if a == b == c:
        print("Equilátero")
    elif a != b != c != a:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os segmentos acima não podem formar um triângulo")


        
            