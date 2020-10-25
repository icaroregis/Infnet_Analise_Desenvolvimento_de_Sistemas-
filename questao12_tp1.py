import turtle

turtle.title("Questão 12 TP1")
turtle.shape("turtle")

raio = int(input("Informe o raio:"));

def desenha_circulo(raio):
    turtle.circle(raio)
        
desenha_circulo(raio)