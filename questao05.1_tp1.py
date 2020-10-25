times = ("Fortaleza", "Ceará", "Palmeiras", "Flamengo", "São Caetano")
time_existe_ou_nao = str(input("Digite um time: "));

def existe_ou_nao(times):
    time_existe = False;
    for c in range(len(times)):
        if (time_existe_ou_nao in times):
            time_existe = True;
            break;
    return time_existe

print("Destino Existe?", existe_ou_nao(times));
print("Esta na posição: {}".format(times.index(time_existe_ou_nao)))
    
        
            
    

