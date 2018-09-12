###########################
# Visão Computacional     #
# Filipe Borba            #
# 6 Semestre              #
# Engenharia da Computação#
###########################

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

# O programa acessa a webcam e tira uma foto, guardando na variável old_frame
ret, old_frame = cap.read()

#Tamanho inicial do centro da imagem
# 640, 480 no caso da minha webcam
xi = 230
xf = 400
yi = 200
yf = 400

#Transforma a primeira foto em escala de cinza
old_gray = cv.cvtColor(old_frame[yi:yf, xi:xf], cv.COLOR_BGR2GRAY)

#Variáveis para acumulação das médias dos fluxos ópticos
flux_x = 0
flux_y = 0

#Variáveis para ajuste do aspect ratio
d_x = 0
d_y = 0

initial_x = 0
initial_y = 0

while(1):
    #Captura novo frame e converte para escala de cinza
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame[yi:yf, xi:xf], cv.COLOR_BGR2GRAY)

    #Cálculo do fluxo óptico
    """
    Por que usar o Dense Optical Flow e não Lucas-Kanade?
    R: O Lucas-Kanade se baseia no cv.goodFeaturesToTrack, que acaba pegando pontos que não fazem parte do centro da imagem, assim, a média do fluxo óptico acaba sendo suavizada e a estabilização fica apenas parcial ou falha.
    """
    flow = cv.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 80, 3, 5, 1.1, 0)
    
    #Cálculo da média do fluxo óptico
    optical_flux_mean = np.mean(np.mean(flow, axis=0), axis=0)

    #Acúmulo da média do fluxo óptico
    flux_x = flux_x - optical_flux_mean[0]
    flux_y = flux_y - optical_flux_mean[1]
    
    #Desenho de um retângulo para ver o centro
    cv.rectangle(frame,(xi,yi),(xf,yf),(0,255,0),3)

    #Estabilização
    """
    O cálculo do fluxo óptico ocorre na área delimitada pelo retângulo.
    A média do fluxo óptico serve para verificar os movimentos na direção x e y.
    Essa verificação é necessária para que exista uma compensação do movimento, e a imagem
    se desloque através do warpAffine, tentando deixar a área de interesse (o retângulo), no
    centro da janela.
    O warpAffine deixa uma borda preta por causa da compensação, que tem de ser removida
    através do Scaling.
    """
    rows,cols, d = frame.shape
    M = np.float32([[1,0,flux_x],[0,1,flux_y]])
    frame = cv.warpAffine(frame,M,(cols,rows))

    #Scaling
    """
    Para efetuar o scaling, precisamos identificar as bordas pretas criadas pela estabilização. Pensando no canto superior esquerdo como a origem (0,0) e o canto inferior direito como o final da imagem (640, 480), precisamos cortar a imagem de acordo com o fluxo óptico. Contudo, o fluxo óptico não irá manter o aspect ratio da imagem, então precisamos colocar mais uma variável para que haja uma compensação do corte. Essa variável é essencial a fim de manter a proporção da imagem, dando a sensação de que estamos dando um zoom nela, sem mostrar as bordas pretas.
    O final da imagem é limitado pelas variáveis new_x e new_y, ou seja, só de criarmos as variáveis dessa forma, já eliminamos o problema das bordas pretas da direita e de baixo da imagem aparecerem. Contudo, as bordas de cima e da esquerda ainda aparecerem, pois não estamos cortando a imagem perto da origem. Para tanto, precisamos das variáveis d_x e d_y, que servem para cortar uma parte extra da imagem, mantendo a proporção. Com isso, o ponto da origem é deslocado de forma a acompanhar o fluxo óptico em x e y, além da compensação, assim como o ponto do final da imagem. Dessa forma, a imagem ficará estabilizada e centrada no quadrado, sem aparecerem as bordas pretas no entorno.
    """
    #Novo final de imagem dado o fluxo óptico
    new_x = 640 - abs(flux_x)
    new_y = 480 - abs(flux_y)

    #Variáveis de Compensação
    if (640/480) > (new_x/new_y):
        d_y = -(3/4) * new_x + new_y
    else:
        d_x = -(4/3) * new_y + new_x
    
    #Corte da Imagem
    initial_x = int(abs(flux_x + d_x))
    initial_y = int(abs(flux_y + d_y))
    final_x = int(min(640, new_x - d_x))
    final_y = int(min(480, new_y - d_y))
    frame = frame[initial_y:final_y, initial_x:final_x]

    #Manutenção do tamanho original
    frame = cv.resize(frame, (640, 480))

    #Renderização da imagem e break caso aperte esc
    cv.imshow('frame', frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

    #Atualização da posição do quadrado e área de interesse
    xi = int(230 - flux_x)
    xf = int(400 - flux_x)
    yi = int(200 - flux_y)
    yf = int(400 - flux_y)

    #O novo frame vira o velho, para que possamos pegar o próximo
    old_gray = frame_gray.copy()

cv.destroyAllWindows()
cap.release()