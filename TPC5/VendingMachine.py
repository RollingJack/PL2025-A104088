import json
import re
import ply.lex as lex

tokens = [
    'LISTAR',
    'SAIR',
    'SALDO',
    'MOEDA',
    'SELECIONAR',
    'ADICIONAR'
]

def t_ADICIONAR(t):
    r'ADICIONAR (.+)'
    produto_info = t.value[10:].split(",")
    cod_produto, nome_produto, preco, quant = produto_info
    preco = float(preco.strip())
    quant = int(quant.strip())
    
    for produto in t.lexer.data['stock']:
        if produto['cod'] == cod_produto.strip():
            produto['quant'] += quant
            print(f"Produto atualizado: {produto['nome']}, Quantidade: {produto['quant']}")
            return t
    t.lexer.data['stock'].append({"cod": cod_produto.strip(), "nome": nome_produto.strip(), "quant": quant, "preco": preco})
    print(f"Produto adicionado: {nome_produto.strip()}, Quantidade: {quant}")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR (.+)'
    cod_produto = t.value[11:].strip()
    produto_encontrado = None
    for produto in t.lexer.data['stock']:
        if produto['cod'].strip() == cod_produto:
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        if produto_encontrado['quant'] > 0:
            if t.lexer.saldo >= produto_encontrado['preco']:
                t.lexer.saldo -= produto_encontrado['preco']
                produto_encontrado['quant'] -= 1
                print(f"Produto dispensado: {produto_encontrado['nome']}")
            else:
                print(f"Saldo insuficiente para satisfazer o seu pedido")
                print(f"Saldo = {round(t.lexer.saldo, 2):.2f}€; Pedido = {produto_encontrado['preco']}€")
        else:
            print(f"Produto {produto_encontrado['nome']} fora de estoque")
    else:
        print("Produto não encontrado")
    return t

def t_MOEDA(t):
    r'MOEDA (.+)'
    moedas = t.value[6:].split(", ")
    total = 0
    for moeda in moedas:
        valor = moeda.strip(' .')
        if valor == '1e':
            total += 1.0
        elif valor == '2e':
            total += 2.0
        elif valor == '50c':
            total += 0.5
        elif valor == '20c':
            total += 0.2
        elif valor == '10c':
            total += 0.1
        elif valor == '5c':
            total += 0.05
        else:
            print(f"Moeda desconhecida: {valor}")
    t.lexer.saldo += total
    print(f"Saldo = {round(t.lexer.saldo, 2):.2f}€")
    return t

def t_SALDO(t):
    r'SALDO'
    print(f"Saldo = {round(t.lexer.saldo, 2):.2f}€")
    return t

def t_LISTAR(t):
    r'LISTAR'
    print("""maq:
cod | nome | quantidade |  preço
------------------------------------""")
    for produto in t.lexer.data['stock']:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | Preço: {produto['preco']}€")
    return t

def t_SAIR(t):
    r'SAIR'
    troco = round(t.lexer.saldo, 2)
    moedas = [1.0, 0.5, 0.2, 0.1, 0.05]
    troco_moedas = {1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0}

    for moeda in moedas:
        while troco >= moeda:
            troco -= moeda
            troco_moedas[moeda] += 1
            troco = round(troco, 2)

    troco_msg = []
    for moeda, quantidade in troco_moedas.items():
        if quantidade > 0:
            troco_msg.append(f"{quantidade}x {str(int(moeda * 100))}c" if moeda < 1 else f"{quantidade}x {int(moeda)}e")

    troco_str = ', '.join(troco_msg)
    print(f"maq: Pode retirar o troco: {troco_str}")
    print(f"maq: Até à próxima")
    with open("stock.json", "w") as file:
        json.dump(t.lexer.data, file, indent=4)
    
    t.lexer.flag = 1
    return t

def t_error(t):
    print(f"Comando inválido: {t.value}")
    t.lexer.skip(1)

def main():
    lexer = lex.lex()

    try:
        with open("stock.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"stock": []}
    
    lexer.data = data
    lexer.flag = 0
    lexer.saldo = 0

    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while lexer.flag == 0:
        input_user = input(">> ")
        lexer.input(input_user)
        token = lexer.token()
        if not token:
            print("Comando inválido")

if __name__ == "__main__":
    main()
