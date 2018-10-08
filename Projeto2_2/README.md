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

#### Estrutura Codebook

#### Subtração de Plano de Fundo

## Resultados

## Conclusão
