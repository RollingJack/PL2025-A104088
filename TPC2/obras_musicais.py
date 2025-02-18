import re
import os

darq = "obras.csv"

compositores = set()
obras_por_periodo = {}
titulos_por_periodo = {}

with open(darq, "r", encoding="utf-8") as f:
    conteudo_errado = f.readlines()

linha1 = conteudo_errado[0]
resto = "".join(conteudo_errado[1:])

corrigido = re.sub(r'\n\s+', ' ', resto)

if not os.path.exists("resultado.txt"):
    with open ("resultado.txt", "w", encoding="utf-8") as resultado:
        resultado.write("Resultados obtidos através do ficheiro obras.csv:\n")

with open("obras_organizadas.csv", "w", encoding="utf-8") as csv:
    csv.write(linha1)
    csv.write(corrigido)

with open("obras_organizadas.csv", "r", encoding="utf-8") as csv:
    ler = csv.read()
    
limitec = r';\d{4};.*?;(.*?);'

for obra in ler.split("\n"):
    obra = obra.strip()

    limitado = re.search(limitec,obra)

    if limitado:
        compositor = limitado.group(1).strip()

        if "," in compositor:
            partes = compositor.split(",", 1)
            compositor = f"{partes[1].strip()} {partes[0].strip()}"

        if compositor not in compositores:
            compositores.add(compositor)

compositores_ordenados = sorted(compositores)

with open("resultado.txt", "a", encoding="utf-8") as resultado:
    resultado.write("Lista ordenada de compositores: " + str(compositores_ordenados) + "\n\n")

limitep = r';\d{4};(.*?);'

for obra in ler.split("\n"):
    obra = obra.strip()

    limitado2 = re.search(limitep,obra)

    if limitado2:
        periodo = limitado2.group(1).strip()
        if periodo:
            obras_por_periodo[periodo] = obras_por_periodo.get(periodo,0) + 1

with open("resultado.txt", "a", encoding="utf-8") as resultado:
    resultado.write("Distribuição das obras por período:\n")

    for periodo, quantidade in obras_por_periodo.items():
        resultado.write(f"{periodo}: {quantidade} obras\n")

    resultado.write("\n")

limited = r'^(.+?);(.+?);\d{4};(.+?);'

for obra in ler.split("\n"):
    obra = obra.strip()

    limitado3 = re.search(limited,obra)

    if limitado3:
        nome = limitado3.group(1).strip()
        periodo = limitado3.group(3).strip()

        titulos_por_periodo[periodo] = titulos_por_periodo.get(periodo, []) + [nome]

for periodo, titulos in titulos_por_periodo.items():
    titulos.sort()

with open("resultado.txt", "a", encoding="utf-8") as resultado:
    resultado.write("Dicionário de títulos das obras por período:\n")

    for periodo, titulos in titulos_por_periodo.items():
        resultado.write(f"{periodo}: {len(titulos)} obras\n")

        for titulo in titulos:
            resultado.write(f" · {titulo}\n")

    resultado.write("\n")



