import turtle

turtle.title("QUESTÃO 18 TP1!")

turtle.shape('turtle')

x = 1
while (x < 8):
    for cont in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.left(60)
    x+=1