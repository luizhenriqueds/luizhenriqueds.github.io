## **Corretor Ortográfico** 

Nesse projeto, iremos implementar três simples modelos de <strong>Corretor Ortográfico</strong>, onde cada um irá receber uma lista de palavras contendo erros gramaticais e irá retornar uma lista de recomendação com cada palavra escrita corretamente.

Para cada palavra escrita errado, o corretor deverá encontrar a palavra que possui a menor distância (sintática) e começa com a mesma letra da palavra errada (em um dicionário de palavras corretas) e irá retornar essa palavra como sugestão.

Cada corretor irá utilizar uma medida de distância entre palavras diferente. Na seção abaixo iremos especificar as medidas de distância utilizadas.

Cada modelo de corretor deverá sugerir palavras corretas para as seguintes palavras disponibilizadas por padrão: `['cormulent', 'incendenece', 'validrate']`.

### **Distância entre palavras**

A distância entre palavras é uma técnica utilizada no Processamento de Linguagem Natural para encontrar palavras similares sintaticamente. Duas medidas de distância muito utilizadas são **Jaccard** e **Levenshtein**. Esse projeto implementa três modelos utilizando essas distâncias.  

#### **Distância de Jaccard**

Para esse corretor, iremos recomendar palavras corretas para as palavras sintaticamente incorretas utilizando a seguinte medida de distância: **[Jaccard distance](https://en.wikipedia.org/wiki/Jaccard_index)**. Dois corretores são implementados com essa técnica, um utilizando 3-grams e outro 4-grams das palavras disponibilizadas.


#### **Distância de Levenshtein**

Para esse corretor, iremos recomendar palavras corretas para as palavras sintaticamente incorretas utilizando a seguinte medida de distância: **[Levenshtein Edit distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)**.

## **Habilidades aplicadas**
Processamento de Linguagem Natural, Similaridade entre palavras

O código do corretor pode ser encontrado nesse endereço: https://tinyurl.com/y6umsrnj.