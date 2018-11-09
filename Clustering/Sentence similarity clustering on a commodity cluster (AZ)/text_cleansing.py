''' Data Cleansing class.

    Remove as palavras presente em um dicionário customizado, que não são úteis para análise dos dados), aplica a função word tokenize do NLTK para cada nome
    de produto, e executa outras funções de formatação, como: lower() e isalpha() nos tokens formatados. O resultado é a junção das palavras tokenizada e limpas
    como uma única linha.

     @author
     
     Bruno Marcos
     Luiz Henrique
     Westerley Reis

     '''

# Importing libraries
from nltk.tokenize import word_tokenize
from pyspark import SparkContext
from pyspark import SQLContext
import os

def word_tokenizer(text):
    
    '''
        Description: Esta função remove stopwords e palavras desnecessárias para análise.
        
        Args: 
            - text (string): recebe cada linha do arquivo
        
        Returns: 
            - joined_tokens (string): retorna o texto normalizado
        
    '''
    
    # Palavras a serem removidas para cada produto
    dictionary = ["gr", "kg", "und", "un", "ml", "lts", "l", "g", "qtd", "qtde", "pt", "cm", "lt", "pc", "pcs", "cp", "pte","fem", "ks", "hw", "br",
                  "preto", "branco", "verde", "azul", "rosa", "vermelho", "roxo", "ref", "gg", "pp", "cor", "dourado", "nude", "colorida"]

    # Tokenização dos itens
    tokens = word_tokenize(text, language='portuguese')

    # Aplica a função na string normalizada, por exemplo, lower case, comprimento > 1, e verificação se é alfanumérico
    tokens = [w.lower() for w in tokens if w.lower() if w.isalpha() if w.lower() not in dictionary if len(w.lower()) > 1]

    # Faz a concatenação dos tokens
    joined_tokens = ' '.join(tokens)
    
    # Retorna os itens como uma unica linha
    return joined_tokens


def cleanse_file(file_order):
    
    '''
        Description: Esta função remove stopwords e palavras desnecessárias para análise para cada arquivo passado como parâmetro.
        
        Args: 
            - file_order (string): índice do arquivo a ser processado 
        
        Returns: N/A
        
    '''

    def format_string_or_return(string):
        
        '''
        Description: Função aplicada para normalizar cada linha do arquivo original, utilizando RDD no Spark.
         
        Args: 
            - text (string): recebe cada linha do arquivo
        
        Returns: 
            - retorna a linha do arquivo normalizada
        
        '''

        delimiter = ' | '

        name_product_string = string.split('|')[3]
        name_normalized = word_tokenizer(name_product_string.strip())
        line = string.split('|')

        # Se o nome do produto for vazia após o processo de limpeza, somente retorna o nome original sem nenhuma alteração
        if name_normalized == '':
            return line[0] +delimiter+ line[1].strip() +delimiter+ line[2].strip() +delimiter+ line[3].strip() +delimiter+ name_product_string.lower().strip()
        else:
            return line[0] +delimiter+ line[1].strip() +delimiter+ line[2].strip() +delimiter+ line[3].strip() +delimiter+ name_normalized

    # Carrega o arquivo como um Spark RDD (Resilient Distributed Dataset)
    rdd = sc.textFile('/home/ladesp/PyCharmProjects/text_clustering/datasets/rp_pagina_'+file_order+'.txt', 100)

    # Gera um novo arquivo que é utilizado para salvar os resultados
    file_nfe_formatted = open('/home/ladesp/PyCharmProjects/text_clustering/formated_datasets/NFE_'+file_order+'_FORMAT.txt', 'w+', encoding='UTF-8')

    # Aplica a função format_string_or_return() para cada produto e retorna o resultado e o salva no arquivo de texto mencionado acima
    for item in rdd.map(lambda x: format_string_or_return(x)).collect():
        file_nfe_formatted.write(item)
        file_nfe_formatted.write('\n')
    file_nfe_formatted.close()

if __name__ == '__main__':
    # Carrega o IP do master local
    SPARK_LOCAL_IP = 'spark://10.1.1.18:7077'

    # Cria um contexto do Spark para iniciar o cluster
    sc = SparkContext(SPARK_LOCAL_IP)
    sql_context = SQLContext(sc)

    # Passa o número de arquivos para serem limpos na função `cleanse_file`
    for item in range(1, 57):
        cleanse_file(str(item))
