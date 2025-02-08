# Somador On/Off

**Data:** 8 de Fevereiro de 2025

**Autor:**  
Nome: André Sousa Miranda  
Número: a104088  
![Foto](image/AndreMiranda.png)

## Resumo
Este projeto tem como objetivo implementar um programa em Python capaz de somar números encontrados dentro de um texto, seguindo um conjunto de regras específicas. O programa começa no estado ligado e, ao encontrar a string "Off", interrompe a soma dos números subsequentes. Caso encontre a string "On", a soma retoma a estar ligada. Quando o caractere "=" aparece no texto, o programa exibe o resultado da soma acumulada.

A lógica foi implementada sem o uso de expressões regulares, o que garante que cada caractere seja processado individualmente. O código percorre a string de entrada, identificando números e controlando o estado da soma conforme as palavras-chave "On" e "Off" aparecem. Os caracteres não numéricos são ignorados, a menos que sejam comandos que alterem o funcionamento do programa.

O projeto foi estruturado em dois arquivos principais:
- **`somador_on_off.py`**: Contém a implementação da função principal e a execução via `main`.
- **`testes.py`**: Permite ao usuário rodar testes predefinidos ou inserir entradas personalizadas.

O programa foi testado com diversas entradas para verificar sua precisão e aderência às regras estabelecidas. Os resultados obtidos confirmam que a implementação atende aos requisitos especificados, garantindo o correto funcionamento das operações de soma e controle de estado.

## Lista de Resultados
- [Código Python](somador_on_off.py)
- [Código para executar exemplos de uso](testes.py)
- [Este manifesto (README.md)](README.md)

## Exemplo de Uso 1
### Entrada:
```
12abc34On56OfF78On90=
```
### Saída esperada:
```
192
```

## Exemplo de Uso 2
### Entrada:
```
10On20Off30On40=
```
### Saída esperada:
```
70
```

## Exemplo de Uso 3
### Entrada:
```
5On10OffOff20On30Off40On50=
```
### Saída esperada:
```
95
```

## Exemplo de Uso 4
### Entrada:
```
Off10On20Off30On40=
```
### Saída esperada:
```
60
```

## Exemplo de Uso 5
### Entrada:
```
On123abc456OFf789On100=
```
### Saída esperada:
```
679
```

## Exemplo de Uso 6
### Entrada:
```
ON50oN60Off70=
```
### Saída esperada:
```
110
```

---


