a = int(input("Digite sua idade somente em anos: "));
m = int(input("Digite sua idade somente em meses: "));
d = int(input("Digite sua idade somente em dias: "));

def conversor_de_anos_dias(a, m, d):
    dias = a * 365
    m = m * 30
    qtde_de_dias = dias + m + d
    return dias

print("Sua idade convertida para dias é {}".format(conversor_de_anos_dias(a, m, d)));