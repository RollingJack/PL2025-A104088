def somador_on_off(texto):
    soma = 0
    ligado = True  
    numero_atual = ""
    i = 0
    texto = texto.lower()  

    while i < len(texto):
        char = texto[i]

        if char.isdigit():
            numero_atual += char  
        else:
            if numero_atual:  
                if ligado:
                    soma += int(numero_atual)
                numero_atual = ""  

            if char == '=':
                print(soma)

            elif texto[i:i+3] == "off":  
                ligado = False
                i += 2  

            elif texto[i:i+2] == "on":  
                ligado = True
                i += 1  

        i += 1  

    
    if numero_atual and ligado:
        soma += int(numero_atual)

if __name__ == "__main__":
    from testes import executar_testes
    executar_testes()