# Católica de Santa Catarina (Fundação Educacional Regional Jaraguaense (FERJ))
## Disciplina de Algoritmos Avançados

Professor: Glauco Scheffel (https://www.linkedin.com/in/glaucoscheffel/)
Aluna: Kamylla Jawad (https://www.linkedin.com/in/kamylla-jawad27/)


<h3>Atividade 1</h3> 

<i>Problema:</i> Faça um programa que leia a lista de nomes masculinos e femininos dos arquivos disponibilizados em https://github.com/MedidaSP/nomes-brasileiros-ibge e carregue em uma lista. A lista deve ser ordenada usando o método de ordenação da linguagem.

Após os dados terem sido lidos e carregados na memória faça o programa solicitar para o usuário um nome e procurar se o nome existe na lista indicando em que posicao ele foi encontrado ou indicando que o nome não existe.

A busca deve ser implementada usando busca binária.


<i>Resolução:</i> 

Foi definido variáveis com um valor mínimo, médio e máximo.
O começo da execução da busca binária começa na metade da lista, se o item dentro da repetição de busca for maior ou menor que o item médio, vai ser definido médio = +/-1 como um novo ponto e um novo ponto máximo ou mínimo, e assim ira se repetir até encontrar o valor desejado

<i>Complexidade:</i> O(log n) -> Cada repetição reduz a área de pesquisa pela metade.

<hr>

<h3>Atividade 2</h3> 

<i>Problema:</i> Mesmo problema da primeira atividade, com o requisito de ser resolvido com complexidade O(1)

<i>Resolução:</i> Tratado o dataset como dicionario, de forma que haja uma ordenação, resete o indice e inverta a chave valor no caso da busca for feita por nome e não por indice.

<i>Complexidade:</i> O(1) -> A implementação interna do dicionário usa tabelas hash, então tem complexidade O(1) para encontrar o índice.

<hr>

<h3>Atividade 3</h3> 

<i>Problema:</i> Mesmo problema da primeira atividade, com o requisito de ser resolvido em paralelo.

<i>Resolução:</i> É retulizado o algoritmo de busca da primeira atividade, porém com implementação de 2 threads de busca para cada sexo.

As threads são inicializadas passando os parâmetros de busca e finalmente são sincronizadas com join().

<i>Complexidade:</i> O((logn)/2)

<hr>

<h3>Atividade 4</h3> 

<i>Problema:</i> Dada uma matriz de tamanho N. A tarefa é ordenar os elementos da matriz completando funções heapify() e buildHeap() que são usadas para implementar Heap Sort.

Sugestão de dado para importar e ordenar https://www.kaggle.com/datasets/sveta151/tiktok-popular-songs-2019

<i>Resolução:</i> A função de heapsort faz a ordenação da array para o valor máximo, reiterando dentro do array o elemento com a chamada do heapify(função), assim ordenando o elemento dentro da array que está sendo estruturado como árvore.

<i>Complexidade:</i> O(nlogn) -> Cenário do pior caso: Ir da base de uma raíz até a oposta

<hr>

<h3>Atividade 5</h3> 

<i>Problema:</i> Você recebe uma matriz unidimensional que pode conter tanto inteiros positivos quanto negativos, encontra a soma de subarranjos contíguos de números que tem a maior soma.


<i>Resolução:</i> Foi usada uma abordagem similar ao merge sort, dividindo a array principal em duas partes iguais após calcular o ponto médio. Sabendo que a array com a maior soma está à direita, esquerda ou passando pelo meio da array principal, foi usada a recursividade pra pegar a soma das possibilidades e juntar no resultado.

Foi utulizado o método de merge sort, premeiro foi calculo o ponto médio para depois dividir em duas partes iguais a array primária. A array com maior soma poderá estar ser posicionada na direita, esquerda ou no ponto médio da array primária, então foi utilizado um método recursivo para somar as possibilidades e no final agrupa-las.

<i>Complexidade:</i> O(nlogn)


