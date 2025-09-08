import turtle
t = turtle.Turtle()
tela = turtle.Screen()
velocidade = 15

def mover_para_cima():
    y = t.ycor()
    t.sety(y + velocidade)

def mover_para_direita():
    x = t.xcor()
    t.setx(x + velocidade)

def mover_para_baixo():
    y = t.ycor()
    t.sety(y - velocidade)

def mover_para_esquerda():
    x = t.xcor()
    t.setx(x - velocidade)

def mover_diagonal_direita_superior():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x + 10, y + 10) )

def mover_diagonal_esquerda_superior():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x - 10, y + 10) )

def mover_diagonal_direita_inferior():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x + 10, y - 10))


def mover_diagonal_esquerda_inferior():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x - 10, y - 10))

def engrossar_linha():
    grossura_linha = t.pensize()
    t.pensize(grossura_linha + 10)

def afinar_linha():
    grossura_linha = t.pensize()
    t.pensize(grossura_linha - 1 < 0)


def borracha():
    cor_fundo = tela.bgcolor()
    cor_caneta = t.pen()["pencolor"]

    if cor_fundo == cor_caneta:
        t.color("black")
        t.shape("classic")
    else:
        t.color(cor_fundo, "gray")
        t.shape("circle")
        t.pensize(15)
          
seguidora = turtle.Turtle()
tela.addshape("south-park.gif")
seguidora.shape("south-park.gif")
seguidora.color("green")
seguidora.pensize(2)
velocidade_seguidora = 5

def mover_seguidora():
    seguidora_x = seguidora.xcor()
    seguidora_y = seguidora.ycor()
    player_x = t.xcor()
    player_y = t.ycor()
    
    if abs(player_x- seguidora_x) > velocidade_seguidora:
        if player_x > seguidora_x:
            seguidora_x = seguidora_x + velocidade_seguidora
        elif player_x == seguidora_x:
            seguidora_x = player_x    
        else:
            seguidora_x = seguidora_x - velocidade_seguidora   
    else:
        seguidora_x- player_x

    if abs(player_y - seguidora_y) > velocidade_seguidora: 
        if player_y > seguidora_y:
            seguidora_y = seguidora_y + velocidade_seguidora
        elif player_y == seguidora_y:
            seguidora_y = player_y   
        else:
            seguidora_y = seguidora_y - velocidade_seguidora

    seguidora.setposition(seguidora_x, seguidora_y)
    tela.ontimer(mover_seguidora, 100)   



tela.listen()

tela.onkeypress(mover_para_cima, "w") 
tela.onkeypress(mover_para_baixo, "s") 
tela.onkeypress(mover_para_direita, "d") 
tela.onkeypress(mover_para_esquerda, "a") 
tela.onkeypress(mover_diagonal_direita_superior, "e") 
tela.onkeypress(mover_diagonal_esquerda_superior, "q") 
tela.onkeypress(mover_diagonal_direita_inferior, "c") 
tela.onkeypress(mover_diagonal_esquerda_inferior, "z") 
tela.onkeypress(borracha, "b")
tela.onkeypress(engrossar_linha, "m")
tela.onkeypress(afinar_linha, "-")
mover_seguidora()
tela.mainloop()  


