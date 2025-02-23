# Conversor MarkDown para HTML

**Data:** 22 de Fevereiro de 2025

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo
Este projeto tem como objetivo criar um conversor simples de MarkDown para HTML, utilizando Python. O conversor processa um arquivo MarkDown e converte os elementos comuns de marcação, como cabeçalhos, negrito, itálico, listas numeradas, links e imagens, para o formato HTML correspondente.

A principal função do programa é ler o conteúdo MarkDown de um arquivo, aplicar as conversões usando expressões regulares e então gerar o arquivo HTML. O código foi desenvolvido de forma modular e eficiente, utilizando apenas a biblioteca padrão do Python, sem dependências externas.

## Funcionamento do Programa
O funcionamento do programa baseia-se na leitura e transformação de um arquivo MarkDown. Primeiramente, o código lê o arquivo de entrada, que contém o conteúdo em MarkDown. Ele então processa o texto linha por linha, procurando por padrões específicos de marcação, como cabeçalhos (identificados pelos sinais `#`), negrito (com `**`), itálico (com `*`), listas numeradas (com números seguidos de ponto), links e imagens.

Para cada padrão encontrado, o programa realiza uma substituição das suas tags HTML correspondentes. Por exemplo, um cabeçalho de primeiro nível, identificado pelo símbolo `#`, é substituído pela tag `<h1>`. As listas numeradas, que começam com `1.`, `2.`, etc., são transformadas em uma lista ordenada (`<ol>`), com cada item representado pela tag `<li>`.

Além disso, o programa lida com imagens e links, que são convertidos para as tags `<img>` e `<a>`, respectivamente. O texto que estiver entre dois asteriscos (`**`) é transformado em negrito, e o texto entre asteriscos simples (`*`) é convertido em itálico.

Depois que todas as substituições são feitas, o código retorna o texto em HTML pronto para ser gravado em um novo arquivo. Esse arquivo HTML pode ser visualizado em qualquer navegador, com o conteúdo formatado corretamente de acordo com as regras de HTML.

O programa foi estruturado de forma simples, utilizando a biblioteca padrão `re` do Python para processar as expressões regulares. Com isso, não é necessário instalar pacotes adicionais, tornando a solução fácil de usar em qualquer ambiente Python.

## Estrutura do Código
O código está organizado de maneira a ser facilmente compreendido e expandido. A função principal, `markdown_para_html`, recebe o texto MarkDown e o converte para HTML. Para realizar as substituições, ela utiliza a função `re.sub` da biblioteca `re`, que permite substituir um padrão identificado por uma expressão regular por um texto especificado.

A primeira parte do código lida com os cabeçalhos. Ele verifica se uma linha começa com um ou mais símbolos `#` e, com base nisso, substitui o cabeçalho correspondente pela tag HTML apropriada. Por exemplo, uma linha iniciada com `#` é transformada em uma tag `<h1>`, enquanto uma linha iniciada com `##` é convertida para uma tag `<h2>`. Essa verificação é feita utilizando a flag `re.MULTILINE`, que permite que o padrão seja aplicado em cada linha individualmente do texto, ao invés de apenas na primeira linha.

Em seguida, o código lida com as marcações de negrito e itálico. Para o negrito, ele usa a expressão regular `\*\*(.*?)\*\*`, que captura qualquer conteúdo entre dois pares de asteriscos duplos (`**`) e o substitui pela tag `<b>`. Para o itálico, a expressão regular `\*(.*?)\*` captura o conteúdo entre asteriscos simples (`*`) e o substitui pela tag `<i>`.

A próxima parte do código trata das listas numeradas. Ele usa uma expressão regular mais complexa para identificar padrões como `1. Primeiro item`, `2. Segundo item`, etc., e agrupar os itens dentro de uma lista ordenada (`<ol>`), com cada item sendo envolvido pela tag `<li>`.

Links e imagens são tratados por expressões regulares que capturam o formato `![texto](url)` para imagens e `[texto](url)` para links, substituindo-os pelas tags HTML `<img>` e `<a>`, respectivamente.

Após realizar todas as substituições necessárias, o texto é retornado como HTML. Caso o código seja expandido para suportar outros elementos de MarkDown, basta adicionar novas expressões regulares para capturar os novos padrões e substituí-los pelas tags HTML correspondentes.

## Resultados

- [Código Python](markdown_para_html.py): Contém a implementação do conversor de MarkDown para HTML.
- [Exemplo de arquivo MarkDown](teste.md): Um arquivo MarkDown com conteúdo de exemplo para teste.
- [Arquivo HTML gerado](saida_do_teste.html): Exemplo de arquivo HTML gerado após a conversão do arquivo MarkDown.

A implementação foi feita de maneira modular e simples, sem o uso de bibliotecas externas, focando apenas no essencial para gerar HTML a partir de MarkDown.

## Exemplo de Uso

### Entrada:
```
# Exemplo de Cabeçalho 1
## Exemplo de Cabeçalho 2
### Exemplo de Cabeçalho 3

Este é um **exemplo** de texto com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com).
```

### Saída esperada:
```
<h1>Exemplo de Cabeçalho 1</h1>
<h2>Exemplo de Cabeçalho 2</h2>
<h3>Exemplo de Cabeçalho 3</h3>

Este é um <b>exemplo</b> de texto com <b>negrito</b> e <i>itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>.

Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>.
```