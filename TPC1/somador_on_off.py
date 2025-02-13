import sys

def somador_on_off():
    soma = 0
    ligado = True  
    numero_atual = ""
    
    for linha in sys.stdin:
        linha = linha.strip().lower()  
        i = 0
        while i < len(linha):
            char = linha[i]

            if char.isdigit():
                numero_atual += char  
            else:
                if numero_atual:  
                    if ligado:
                        soma += int(numero_atual)
                    numero_atual = ""  

                if char == '=':
                    print(f"A Soma atual é : {soma}")

                elif linha[i:i+3] == "off":  
                    ligado = False
                    i += 2  

                elif linha[i:i+2] == "on":  
                    ligado = True
                    i += 1  

            i += 1  

        if numero_atual and ligado:
            soma += int(numero_atual)
            numero_atual = ""

if __name__ == "__main__":
    somador_on_off()
