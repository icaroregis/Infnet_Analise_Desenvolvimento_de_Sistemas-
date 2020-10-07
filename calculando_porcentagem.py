valor_conta = float(input("Digite o valor da conta:  R$"))
gorjeta = (valor_conta * 10) / 100
valor_final = gorjeta + valor_conta
print("O valor da gorjeta é de R${}".format(gorjeta))
print("O valor total a ser pago é de R${}".format(valor_final))
