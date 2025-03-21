# TCP6 : Gramática Independente de Contexto

**Data:** 17 de Março de 2025

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo

O objetivo é implementar uma Gramática Independente de Contexto para avaliar expressões matemáticas, seguindo as diversas regras gramaticais, para possibilitar a implementação de um parser recursivo descendente e garantir a correta precedência de operadores.

### Exemplos de expressões suportadas:

```
    5 + 3 * 2
    2 * 7 - 5 * 3
```

### Gramática

```bash
    T = {'+', '-', '*', '/', num}
    S = Exp
    N = {Exp, Term, Fat}

P = {
    Exp -> Term '+' Exp
        | Term '-' Exp
        | Term

    Term -> Fat '*' Term
        | Fat '/' Term
        | Fat

    Fat -> num
}
    
```
## Funcionamento do código

O código consiste em dois módulos principais, o analisador léxico e o analisador sintático (Recursivo Descendente).

### Analisador Léxico

O analisador léxico tem a responsabilidade de transformar a entrada, que é uma expressão matemática, em uma sequência de tokens que podem ser compreendidos pelo analisador sintático. Ele utiliza expressões regulares para reconhecer números inteiros e operadores aritméticos (`+`, `-`, `*`, `/`). Além disso, ignora espaços em branco e lida com possíveis erros ao encontrar caracteres desconhecidos.

### Analisador Sintático

O analisador sintático segue um modelo recursivo descendente, implementando a gramática definida. Ele analisa a sequência de tokens gerado pelo analisador léxico e avalia as expressões, respeitando a precedência dos operadores. A estrutura é baseada nos conceitos de fator (`Fat`), termo (`Term`) e expressão (`Exp`), o que garante que as multiplicações e divisões sejam resolvidas antes das somas e subtrações.

O processo de avaliação segue uma abordagem recursiva descendente, onde cada função representa uma regra gramatical e chama outras funções conforme necessário. A execução começa pela análise de uma expressão (`exp`), que verifica se há termos (`term`) seguidos por operadores de soma ou subtração. O termo, por sua vez, trata fatores (`fat`) e gerencia multiplicações e divisões antes de retornar o resultado parcial para a expressão.

Dessa forma, a implementação permite que expressões matemáticas sejam corretamente analisadas e calculadas, respeitando a ordem das operações. Essa abordagem modular facilita a extensão do código para suportar novas funcionalidades, como a inclusão de parênteses para alterar a precedência dos cálculos.


### Resultados

- [anali_lex.py](anali_lex.py): Código do Analisador Léxico
- [anali_sin.py](anali_sin.py): Código do Analisador Sintático

O programa foi desenvolvido de forma modular, permitindo fácil manutenção e atualização do código.

```
Digite a expressão matemática: 5 + 3 * 2
5 + 3 * 2 = 11
Digite a expressão matemática: 2 * 7 - 5 * 3
2 * 7 - 5 * 3 = -1
```