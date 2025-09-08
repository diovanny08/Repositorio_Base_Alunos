import pygame

pygame.init
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

x = 50
y =50
velocidade_x = 5
velocidade_y = 5
largura_ret, altura_ret = 50, 50

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    x += velocidade_x
    y += velocidade_y

    tela.fill((0,0,0))
    pygame.draw.rect(tela, (255,0,255), (x,y, largura_ret, altura_ret))
    pygame.display.update()
    clock.tick(60)

pygame.quit()