# TCP6 : Gramática Independente de Contexto

**Data:** 17 de Março de 2025

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo

Implementar uma Gramática Independente de Contexto para avaliar expressões matemáticas, garantindo a correta precedência de operadores. O objetivo é definir a gramática envolvida para as diversas regras gramaticais, possibilitando a implementação de um parser recursivo descendente.

### Exemplos de expressões suportadas:

```
    5 + 3 * 2
    2 * 7 - 5 * 2
```

### Gramática

```bash
    T = {+, -, *, /, num}
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





