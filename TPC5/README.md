# Máquina de Vending

**Data:** 9 de Março de 2025

# Autor
**Nome:** André Sousa Miranda  
**Número:** a104088  
![Foto](image/AndreMiranda.png)

## Resumo

Este projeto consiste no desenvolvimento de uma máquina de vendas automatizada utilizando Python. A máquina permite que os utilizadores possam ver os produtos em `stock`, insirir moedas, verificar o saldo, fazer compras dos produtos disponíveis em `stock` e retirar o troco. O sistema também permite a administração de produtos através de comandos como "ADICIONAR", "SELECIONAR", "LISTAR", "MOEDA", "SALDO" e "SAIR". O `stock` de produtos é carregado e atualizado a partir de um arquivo JSON.

## Funcionamento do Programa

O programa funciona de forma interativa, lendo comandos fornecidos pelo utilizador e executando ações de acordo com os comandos dados. O programa realiza as seguintes operações:

1. **Inserir Moedas**: O utilizador insere moedas de valores fixos (como `2e`, `1e`, `50c`, `20c`, `10c`, `5c`), que são adicionados ao saldo atual.
2. **Seleção de Produtos**: O utilizador pode selecionar produtos disponíveis em `stock` ao usar o comando `SELECIONAR` e o código do produto.
3. **Consultar o Saldo**: O comando `SALDO` permite que o utilizador consulte o saldo disponível.
4. **Listagem de Produtos**: O comando `LISTAR` exibe todos os produtos disponíveis no `stock`.
5. **Adicionar Produtos**: O comando `ADICIONAR` permite adicionar novos produtos ou atualizar as quantidades de produtos existentes no `stock`.
6. **Saída e Troco**: O comando `SAIR` finaliza a interação e fornece o troco ao utilizador, além de salvar o estado atual do `stock` no arquivo JSON.

Tokens reconhecidos:
- **LISTAR**: Exibe a lista de produtos disponíveis no `stock`.
- **SAIR**: Finaliza a interação e calcula o troco.
- **SALDO**: Exibe o saldo atual.
- **MOEDA**: Permite o utilizador inserir moedas.
- **SELECIONAR**: Permite o utilizador selecionar um produto para comprar.
- **ADICIONAR**: Adiciona ou atualiza produtos em `stock`.

## Estrutura do Código

A principal lógica do programa está na função `lexer` e `ply.lex`, que realiza a leitura dos comandos e aplica as expressões regulares para identificar e categorizar os tokens. O programa contém funções para cada comando, como `t_MOEDA`, `t_SALDO`, `t_SELECIONAR`, entre outros.

1. **Definição de Tokens**: A lista `tokens` contém os tipos de comandos que a máquina reconhece, como `LISTAR`, `SAIR`, `MOEDA`, etc.
2. **Expressões Regulares**: Cada comando é reconhecido por uma expressão regular associada à sua função correspondente.
3. **Funções de Comando**: Cada função lida com a lógica específica de cada comando, seja inserir moedas, exibir o saldo ou realizar compras.
4. **Erros**: Comandos inválidos geram mensagens de erro para o utilizador.

### Tratamento de Erros

Se o sistema encontrar um comando inválido ou um erro na entrada, ele fornecerá uma mensagem que informa que deu erro, por exemplo:

```
Comando inválido
```

## Resultados

- [VendingMachine.py](VendingMachine.py): Implementação completa da máquina de vendas.
- [stock.json](stock.json): Exemplo de arquivo JSON contendo o `stock` da máquina de vendas.

O programa foi desenvolvido de forma modular, permitindo fácil manutenção e atualização do código. A funcionalidade de adicionar novos produtos e atualizar o `stock` também foi implementada de forma dinâmica.

## Exemplo de Uso

### LISTAR:
```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade |  preço
------------------------------------
A23 | Ã¡gua 0.5L | 2 | Preço: 0.7€
B12 | refrigerante 330ml | 5 | Preço: 1.2€
C45 | batata frita | 10 | Preço: 1.5€
D67 | chocolate | 3 | Preço: 2.0€
```

### MOEDA:
```
>> MOEDA 1e, 20c, 5c, 5c .
Saldo = 1.30€
>> MOEDA 1e, 20c, 5c, 5c  
Saldo = 2.60€
```

### SALDO:
```
>> SALDO
Saldo = 2.60€
```

### SELECIONAR:
```
>> SELECIONAR A23
Produto dispensado: Ã¡gua 0.5L
>> SELECIONAR D67
Saldo insuficiente para satisfazer o seu pedido
Saldo = 1.90€; Pedido = 2.0€
```

### ADICIONAR:
```
>> ADICIONAR E30, pepsi, 1.2, 10
Produto adicionado: pepsi, Quantidade: 10
>> LISTAR
maq:
cod | nome | quantidade |  preço
------------------------------------
A23 | Ã¡gua 0.5L | 1 | Preço: 0.7€
B12 | refrigerante 330ml | 5 | Preço: 1.2€
C45 | batata frita | 10 | Preço: 1.5€
D67 | chocolate | 3 | Preço: 2.0€
E30 | pepsi | 10 | Preço: 1.2€
```

### SAIR:
```
>> SAIR
maq: Pode retirar o troco: 1x 1e, 1x 50c, 2x 20c
maq: Até à próxima
```

Este projeto serve como uma introdução prática ao desenvolvimento de sistemas interativos em Python e pode ser facilmente expandido com novas funcionalidades ou ajustes na interface do utilizador.