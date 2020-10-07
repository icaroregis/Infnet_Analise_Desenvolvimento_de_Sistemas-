salario_atual = float(input("Digite seu salário atual: R$"))
salario_ajustado = (salario_atual * 7.3) / 100
salario_final = salario_atual + salario_ajustado
print("O seu salário atual de R${} passou a ser R${:.2f}, com o percentual de acrécimo de 7,3% que equivale a {:.2f}".format(salario_atual, salario_final, salario_ajustado))
