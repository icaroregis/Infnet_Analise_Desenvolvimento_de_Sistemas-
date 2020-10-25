num = int(input("digite numero: "))
_str = input("digite string: ")

aux = _str[:num]
aux2 = _str[num:]
aux3 = aux2 + aux

print (aux3)