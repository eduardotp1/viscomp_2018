# Buscador de Imagens
Filipe Borba - 6º Semestre<br>
Engenharia da Computação Insper<br>
Visão Computacional<br>

## Sumário

- [Como executar](#comoexecutar)

## Como executar

Para fazer um treinamento, é necessário rodar o seguinte comando:

`python3 search_image.py caminho_ate_pasta -t -m 15 -f Faces garfield platypus nautilus elephant gerenuk`

- O caminho_ate_pasta é o argumento OBRIGATORIO para o caminho da pasta que possui as pastas com imagens.
- O comando -t ou --train indica que será realizado um treinamento.
- O comando -m ou --maxitems seguido de um integer determina a quantidade de imagens que serão utilizadas para treino (default 10).
- O comando -f ou --folders determina as pastas que serão utilizadas para o treinamento. Elas devem estar escritas como no exemplo.


Para fazer uma busca de imagem, é necessário rodar o seguinte comando:

`python3 search_image.py caminho_ate_imagem -s`

- O caminho_ate_imagem é o caminho da imagem que o usuário deseja utilizar como busca.
- O comando opcional -s ou --show indica que o programa deve plotar as imagens.