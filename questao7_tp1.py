import turtle

turtle.title("QUESTÃO 7 TP1!")

turtle.shape('turtle')

x = 1
while (x < 5):
    for cont in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(100)
    x+=1
