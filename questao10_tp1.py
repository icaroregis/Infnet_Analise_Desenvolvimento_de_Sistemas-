import turtle

turtle.title("QUESTÃO 10 TP1!")

turtle.shape('turtle')

n = int(4)

def desenha_quadrado(n):
    for count in range(0, n):
        turtle.forward(100)
        turtle.left(90)
        
desenha_quadrado(n)

