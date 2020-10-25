times = ("Fortaleza", "Ceará", "Palmeiras", "Flamengo", "São Caetano", "Bahia")


def divisao_de_times(times):
    dividir_tupla = len(times) // 2;
    time1 = times[:dividir_tupla]
    time2 = times[dividir_tupla:]
    return time1, time2

print("Após a divisão temos respectivamente duas tuplas {}".format(divisao_de_times(times)));

