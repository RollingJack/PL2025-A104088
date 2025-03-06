# Analisador Léxico para Consultas SPARQL

**Data:** 2 de Março de 2025

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo

Este projeto consiste no desenvolvimento de um analisador léxico em Python para processar consultas SPARQL a partir de arquivos `.txt`. O analisador identifica e classifica diferentes tipos de tokens, como números, identificadores, palavras-chave, texto, operadores e símbolos especiais. Utilizando expressões regulares, o código reconhece cada token no conteúdo do arquivo de entrada e os categoriza conforme regras predefinidas.

## Funcionamento do Programa

O programa lê um arquivo contendo uma consulta SPARQL e realiza a análise léxica do conteúdo. Ele utiliza a biblioteca `re` do Python para buscar os padrões definidos e classificar os tokens em diferentes categorias. 

O processo ocorre em três etapas principais:

1. **Leitura do Arquivo**: O conteúdo do arquivo é lido integralmente.
2. **Reconhecimento de Tokens**: Através da correspondência com expressões regulares, cada token é identificado e categorizado.
3. **Enviar a Saída**: Os tokens reconhecidos são armazenados e exibidos, com marcação de erros para caracteres não identificados.

Tokens reconhecidos:
- **COMMENT**: Comentário (ignorado).
- **NUM**: Números inteiros.
- **PA**: Parêntese aberto `(`.
- **PF**: Parêntese fechado `)`.
- **DOT**: Ponto `.`.
- **VIRG**: Vírgula `,`.
- **NEWLINE**: Quebra de linha `\n`.
- **KEYWORD**: Palavras-chave (ex.: `select`, `where`, `LIMIT`, `a`).
- **VAR**: Variáveis SPARQL (ex.: `?nome`, `?desc`).
- **IDENTIFIER**: Identificadores (ex.: `dbo:MusicalArtist`).
- **STRING**: Cadeias de texto entre aspas (ex.: `"Chuck Berry"`).
- **LANGTAG**: Identificadores de língua (ex.: ``@en`)
- **OP**: Operadores (ex.: `=`, `:`,`+`,`/`).
- **ABRE_CH**: Abre chavetas `{`.
- **FECHA_CH**: Fecha chavetas `}`.
- **COMMENT**: Comentários iniciados por `#`.
- **SKIP**: Espaços em branco e tabulações (ignorados).
- **ERRO**: Qualquer carácter não reconhecido.

## Estrutura do Código

A principal lógica do programa está na função `lexer`, que realiza a leitura do arquivo e aplica as expressões regulares. Seguindo esta estrutura realizada:

1. **Definição de Tokens**: A lista `TOKEN_TYPES` contém tuplas com o nome do token e sua expressão regular correspondente.
2. **Compilação da Regex Principal**: As expressões regulares são combinadas em uma única regex através da função `join`.
3. **Análise Léxica**: A função `lexer` percorre o conteúdo do arquivo, identifica os tokens e os armazena em uma lista.
4. **Erros**: Tokens não reconhecidos geram mensagens de erro.

### Tratamento de Erros

Se o analisador encontrar um carácter ou padrão que não se enquadre em nenhuma categoria, ele será classificado como `ERRO`. Por exemplo:

```
Erro léxico: 'X' não reconhecido.
```

## Resultados

- [lexer.py](lexer.py): Implementação completa do analisador léxico.
- [query.txt](query.txt): Exemplo de entrada com a query a ser analisada.

O programa está estruturado para ser fácil de entender e expandir. Novos tipos de tokens podem ser adicionados facilmente atualizando a lista `TOKEN_TYPES` com a expressão regular correspondente.

## Exemplo de Uso

### Entrada (query.txt):
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

### Saída Esperada:
```
('NEWLINE', '\n')
('KEYWORD', 'select')
('VAR', '?nome')
('VAR', '?desc')
('KEYWORD', 'where')
('ABRE_CH', '{')
('NEWLINE', '\n')
('VAR', '?s')
('KEYWORD', 'a')
('IDENTIFIER', 'dbo:MusicalArtist')
('DOT', '.')
('NEWLINE', '\n')
('VAR', '?s')
('IDENTIFIER', 'foaf:name')
('STRING', '"Chuck Berry"')
('LANGTAG', '@en')
('DOT', '.')
('NEWLINE', '\n')
('VAR', '?w')
('IDENTIFIER', 'dbo:artist')
('VAR', '?s')
('DOT', '.')
('NEWLINE', '\n')
('VAR', '?w')
('IDENTIFIER', 'foaf:name')
('VAR', '?nome')
('DOT', '.')
('NEWLINE', '\n')
('VAR', '?w')
('IDENTIFIER', 'dbo:abstract')
('VAR', '?desc')
('NEWLINE', '\n')
('FECHA_CH', '}')
('KEYWORD', 'LIMIT')
('NUM', '1000')
```

