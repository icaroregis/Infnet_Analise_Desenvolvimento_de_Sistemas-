import turtle

turtle.title("QUESTÃO 11 TP1!")

turtle.shape('turtle')

n = int(3)

def desenha_triangulo(n):
    for cont in range(0, n):
        turtle.forward(100)
        turtle.left(120)

desenha_triangulo(n)
    
    