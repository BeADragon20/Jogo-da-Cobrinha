import pygame # importa a biblioteca
from pygame.locals import *
from sys import exit
from random import randint # serve para sortear valores dentro de um determinado intervalo

pygame.init() #inicia a biblioteca

pygame.mixer.music.set_volume(0.09) # mexe no volume da musica de fundo entre 0 e 1
musica_de_fundo = pygame.mixer.music.load('./Musicas/BoxCat Games - Defeat.mp3') # coloca musica de fundo .mp3
pygame.mixer.music.play(-1) # -1 repete a musica sem parar


barulho_colisao = pygame.mixer.Sound('./Musicas/smw_coin.wav') # OBRIGATÓRIO ser .wav
barulho_colisao.set_volume(0.8) # mexe no volume da musica de colisao entre 0 e 1


largura = 640 
altura = 480
x_cobra = int(largura /2) # - 40/2 "o meio" perfeito
y_cobra = int(altura /2)



velocidade = 10

x_controle = 20
y_controle = 0

#                Y    Y
x_maca = randint(40 ,600)
y_maca = randint(50 ,430) 

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True) # variavel para fonte/texto
# para saber todas as fontes disponiveis digite "pygame.font.get_fonts()"


tela = pygame.display.set_mode((largura, altura)) # faz uma tela com o tamanho predefinido
pygame.display.set_caption('Jogo') # muda o nome da janela
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        pygame.draw.rect(tela,(0,255,0), (XeY[0], XeY[1], 20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura /2) # - 40/2 "o meio" perfeito
    y_cobra = int(altura /2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40 ,600)
    y_maca = randint(50 ,430) 
    morreu = False


while True:
    relogio.tick(30) # Velocidade dos frames
    tela.fill((255,255,255)) # Cor da tela de Fundo

    mensagem = f'Pontos: {pontos}' # inicia o nome da variavel
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0)) # formatação da variavel do texto
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 
        if event.type == KEYDOWN: # inicia o evento de clicar no teclado
            if event.key == K_a: # move para a direita sem diagonal
                if x_controle == velocidade:
                    pass
                else:
                    x_controle =- velocidade
                    y_controle =- 0

            if event.key == K_d: # move para a esquerda sem diagonal
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w: # move para a cima sem diagonal
                if y_controle == velocidade:
                   pass
                else:                   
                    y_controle =  - velocidade
                    x_controle = 0
            
            if event.key == K_s: # move para a baixo sem diagonal
                if y_controle == -velocidade:   
                    pass
                else:
                    y_controle = + velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
#            |retangulo|            R  G  B    X  Y   LarPixl AltPixl 
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20)) 

    if cobra.colliderect(maca): # evento para quando se tocarem
        x_maca = randint(40 ,600)
        y_maca = randint(50 ,430)  
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
        velocidade = velocidade + 0.1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True,(0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center= (largura//2,altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    # faz a cobra voltar a tela contraria
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
        
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 40)) # Coloca o texto na tela

    pygame.display.update()  # atualiza a tela
