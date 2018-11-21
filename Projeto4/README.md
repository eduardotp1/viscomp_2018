# Realidade Aumentada
Filipe Borba, Gabriel Moreira, Guilherme Graicer
6º Semestre<br>
Engenharia da Computação Insper<br>
Visão Computacional<br>

## Sumário

- [Como executar](#comoexecutar)
- [Funcionamento](#funcionamento)

## Como executar

Para executar o programa, primeiro, verifique o caminho da imagem a ser substituída, assim como o caminho da imagem aruco_board.png, que deve estar na mesma pasta do programa python.
Com o caminho da imagem de substituição em mãos, basta rodar o seguinte comando:

`python3 detector.py "caminho_ate_imagem"`

- O caminho_ate_imagem é o argumento OBRIGATORIO para o caminho no qual se encontra a imagem.

## Funcionamento

  Primeiramente, o código pega a imagem do tabuleiro aruco digitalizada, detecta os marcadores nela e constrói uma lista com os pontos referentes as pontas dos marcadores. Em seguida ele começa a filmar com a webcam e para cada frame ele: detecta os marcadores do tabuleiro físico (que aperece na imagem da câmera); constrói uma nova lista somente com os pontos da imagem digitalizada que tem o mesmo id dos pontos identificados pela camera; com esses dois conjuntos de pontos calcula-se a *matriz de homografia*; chama a função *warpPerspective* do opencv. Essa última função recebe a imagem escolhida como parâmetro para o programa, aplica a homografia calculada nela, deixando-a com a perspectiva esperada e o resto da imagem ela deixa preta. Finalmente, pintamos o que não for preto dessa imagem sobre o frame atual, gerando a imagem com Realidade Aumentada.


