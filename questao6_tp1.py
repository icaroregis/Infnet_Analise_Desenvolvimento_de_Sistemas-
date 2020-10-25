import turtle

turtle.title("Questão 6 TP1")
turtle.shape("turtle")

def circulo():
    for x in range(0,360,15):
        turtle.setheading(x)
        turtle.forward(100)
        turtle.write(x)
        turtle.backward(100)
        
        
turtle.listen()
circulo()
