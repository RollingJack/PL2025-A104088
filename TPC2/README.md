# Análise de Obras Musicais

**Data:** 16 de Fevereiro de 2025

## Autor

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo

Este projeto tem como objetivo analisar um conjunto de dados que contém informações sobre obras musicais, extraídas de um arquivo CSV. A partir desses dados, o programa identifica e organiza os compositores, classifica as obras de acordo com o período musical a que pertencem e exibe os títulos de cada período em ordem alfabética.

A implementação foi feita em Python sem utilizar o módulo `csv`, garantindo que a leitura e manipulação dos dados fossem feitas diretamente através da manipulação de strings. O código percorre o arquivo linha por linha, separa as informações usando o carácter `;` como delimitador e armazena os resultados em estruturas de dados adequadas, como conjuntos e dicionários.

## Funcionamento do Programa

1. O programa lê o arquivo CSV, ignorando a primeira linha (cabeçalho).
2. As linhas subsequentes são processadas, removendo quebras de linha indevidas.
3. Os nomes dos compositores são extraídos e armazenados em um conjunto para evitar repetições.
4. A contagem das obras por período é realizada utilizando um dicionário, onde a chave representa o período e o valor indica a quantidade de obras associadas.
5. Os títulos das obras são organizados por período e armazenados em um dicionário.
6. As listas de compositores e títulos são ordenadas alfabeticamente.
7. Os resultados são escritos no arquivo `resultado.txt`, incluindo:
   - Lista ordenada de compositores
   - Distribuição das obras por período
   - Dicionário de títulos das obras organizados por período

## Estrutura do Código

O código principal está contido no [Código em Python](obras_musicais.py), que realiza todas as operações descritas acima. A leitura dos dados é feita diretamente através da função `open()` e os valores são processados sem depender de bibliotecas externas para manipulação de CSVs.

## Resultados ou links em falta

[obras.csv](obras.csv) - Este ficheiro csv foi fornecido pelo professor para nós utilizarmos para a resolução deste TPC;

[obras_organizadas.csv](obras_organizadas.csv) - Este ficheiro csv resulta do código `obras_musicais.py`, de forma a que organiza o ficheiro `obras.csv` para que se torne mais acessível e eficiente para o resto do funcionamento do código;

[resultado.txt](resultado.txt) - Este ficheiro possui o resultado obtido do código `obras_musicais.py` a partir do ficheiro `obras_organizadas.csv` para obter o resultado dos três exercícios pedidos;

Caso seja necessário, o código pode ser adaptado para processar arquivos CSV com diferentes formatos de separação ou incluir novas análises sobre as obras listadas. O programa foi desenvolvido para ser eficiente e fácil de modificar, permitindo ampliações futuras.

---



