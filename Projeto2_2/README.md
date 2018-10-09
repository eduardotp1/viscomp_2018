# Segmentação de Primeiro Plano e Plano de Fundo
Filipe Borba - 6º Semestre
Engenharia da Computação Insper
Visão Computacional

## Sumário

- [Introdução](#introducao)
- [Codebook](#codebook)
- [Resultados](#resultados)
- [Conclusão](#conclusao)

## Introdução
Artigo de referência: "Real-time foreground–background segmentation using codebook model"
O objetivo do projeto foi de utilizar o modelo de Codebook para realizar a segmentação de imagens, obtendo um plano de fundo (background) e um primeiro plano (foreground). Apesar de existirem diferentes modelos para isso, como o Mixture of Gaussians ou MOG, o modelo de Codebook oferece, no geral, uma performance melhor do que os outros, como visto no artigo.
Com a técnica aplicada no projeto, é possível realizar a contagem de quantas pessoas passam por um determinado local, o que é interessante para manifestações, por exemplo.

## Codebook
A ideia por trás do modelo de Codebook é criar um elemento chamado de Codeword para cada pixel da imagem. Esse Codeword servirá como referência para que o algoritmo possa identificar mudanças na imagem e julgar se faz parte do primeiro plano ou do plano de fundo. Alguns cálculos são estabelecidos utilizando as cores e brilho dos pixels para construir um novo codeword e inserir no codebook ou apenas atualizar um existente. Com isso, cada pixel não terá o mesmo número de codewords.

### Implementação
#### Funções Auxiliares
O algoritmo do codebook possui duas funções auxiliares: Colordist e Brightness.
A função colordist serve para verificar a distorção de cores de cada pixel da imagem, enquanto que a função brightness visa detectar mudanças no brilho de cada pixel. As duas funções podem ser vistas nas imagens 1 e 2.
![Brightness](https://i.imgur.com/gaJs3LE.png)
Imagem 1 - Função Brightness

![Colordist](https://i.imgur.com/l6JoE1T.png)
Imagem 2 - Função Colordist

#### Estrutura Codebook
Um codebook é basicamente uma lista que contém listas de codewords por pixel. O codeword é composto por um vetor que guarda o valor RGB da imagem e outro vetor que contém valores de brilho entre outras variáveis temporais. Nessa implementação, foram utilizadas tuplas para os dois elementos.
Temos então na tupla RGB:
- r: quantidade de vermelho que o pixel possui.
- g: quantidade de verde que o pixel possui.
- b: quantidade de azul que o pixel possui.
E na tupla Aux:
- min_brightness: menor brilho de todos os pixeis associados a este codeword armazenado
- max_brightness: maior brilho de todos os pixeis associados a este codeword armazenado
- freq: frequência com a qual esse codeword foi coincidido
- mnrl: maior intervalo durante o periodo de treino que o codeword não coincidiu
- first_access: primeira vez que o codeword armazenado coincidiu
- last_access: ultima vez que o codeword armazenado coincidiu

Na imagem 3, verifica-se a implementação dada no artigo.
![Codebook](https://i.imgur.com/OwbGkIj.png)
Imagem 3 - Pseudo-código do Codebook

#### Subtração de Plano de Fundo
Por fim, para realizar a subtração do plano de fundo, o algoritmo utiliza o codebook armazenado e compara o pixel com cada codeword. Assim, se houver coincidência, significa que o pixel faz parte do plano de fundo, caso contrário, faz parte do primeiro plano. Essa dinâmica fica clara com a imagem 4 a seguir.
![Subtracao](https://i.imgur.com/VMW7ljF.png)
Imagem 4 - Pseudo-código da subtração de plano de fundo utilizando o codebook.

## Resultados

