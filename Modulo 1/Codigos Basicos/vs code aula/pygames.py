import pygame
 

pygame.init() #Inicializa os módulos do pygame (vídeo, som e etc...)
largura = 800
altura = 600


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo com Pygame.")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
   
    tela.fill((255,255,255))

    pygame.display.update()

pygame.quit()