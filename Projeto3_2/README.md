# Busca por Imagens Usando Palavras
Filipe Borba - 6º Semestre<br>
Engenharia da Computação Insper<br>
Visão Computacional<br>

## Sumário

- [Como executar](#comoexecutar)
- [Conceitos](#conceitos)

## Como executar

Para executar o programa, primeiro baixe a pasta "helper.zip" do repositório e descompacte-a. Nela, temos a pasta "helper" que possui um modelo pré-treinado do banco de dados. Caso deseje utilizá-lo, não será necessário fazer o treinamento.
Para o caso de treinamento, a pasta "dataset-projeto-3-2" precisa estar na pasta raíz e os comandos devem ser executados.

Para fazer um treinamento, é necessário rodar o seguinte comando:

`python3 search_term.py caminho_ate_pasta/ -t`

- O caminho_ate_pasta é o argumento OBRIGATORIO para o caminho da pasta que possui as pastas com imagens, com uma barra no final.
- O comando -t ou --train indica que será realizado um treinamento.

Para fazer uma busca de termo, é necessário rodar o seguinte comando:

`python3 search_term.py "termo" -s`

- O "termo" é o argumento OBRIGATORIO do termo utilizado para que seja realizada a busca, em aspas.
- O comando opcional -s ou --show indica que o programa deve plotar as imagens.

## Conceitos

A busca de imagens através de termos baseia-se na classificação categórica. A classificação binária, vista no projeto 3-1, classifica imagens em pertencendo ou não a uma classe (cachorros vs faces). Neste projeto, a classificação em categorias foi exercitada e para isto foram usados os modelos de Regressão Logística, Redes Neurais Multi-Nível, Rede Convolucionais e Redes Pré-Treinadas. Para tanto, a biblioteca keras serviu para treinar redes neurais que realizam a classificação categórica de imagens, aplicando o modelo do MobileNet.
Essa classificação é feita através de probabilidades, ou seja, quanto maior a probabilidade da imagem ser de certa classe, muito provável que ela realmente seja daquela classe. Esse princípio serviu de base para separar as imagens do banco de dados "dataset-projeto-3-2" e separá-las em categorias para busca posterior.
