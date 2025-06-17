import pygame
import sys
import random

# Inicializar o pygame
pygame.init()

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tela
LARGURA = 600
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Cobrinha com tela infinita - Aperte ENTER para reiniciar')

# Relógio
clock = pygame.time.Clock()
FPS = 10

# Tamanho do bloco
TAMANHO_BLOCO = 20

# Fonte
fonte = pygame.font.SysFont(None, 35)

# Função para desenhar a cobrinha
def desenhar_cobrinha(blocos):
    for bloco in blocos:
        pygame.draw.rect(TELA, VERDE, (bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

# Função principal do jogo
def jogo():
    x = LARGURA // 2
    y = ALTURA // 2
    x_mudanca = 0
    y_mudanca = 0

    corpo_cobrinha = []
    tamanho_cobra = 1

    comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    rodando = True
    game_over = False

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -TAMANHO_BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = TAMANHO_BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -TAMANHO_BLOCO
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = TAMANHO_BLOCO
                    x_mudanca = 0
                elif evento.key == pygame.K_RETURN:
                    jogo()  # Reiniciar

        if not game_over:
            x += x_mudanca
            y += y_mudanca

            # Passar pelas bordas (wrap around)
            if x < 0:
                x = LARGURA - TAMANHO_BLOCO
            elif x >= LARGURA:
                x = 0
            if y < 0:
                y = ALTURA - TAMANHO_BLOCO
            elif y >= ALTURA:
                y = 0

            corpo_cobrinha.append([x, y])
            if len(corpo_cobrinha) > tamanho_cobra:
                del corpo_cobrinha[0]

            # Verificar colisão com o próprio corpo
            for segmento in corpo_cobrinha[:-1]:
                if segmento == [x, y]:
                    game_over = True

            TELA.fill(PRETO)
            pygame.draw.rect(TELA, BRANCO, (comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
            desenhar_cobrinha(corpo_cobrinha)

            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
                comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

        else:
            texto = fonte.render("Você perdeu! Aperte ENTER para reiniciar", True, VERMELHO)
            TELA.blit(texto, [LARGURA / 6, ALTURA / 2.5])

        pygame.display.update()
        clock.tick(FPS)

# Iniciar o jogo
jogo()
