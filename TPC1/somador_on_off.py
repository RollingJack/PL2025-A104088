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
    from testes import rodar_testes
    rodar_testes()

#
# Exemplos de uso de resultados:
#entrada = "12abc34On56OfF78On90="
#somador_on_off(entrada)  # Deve imprimir 192 

#entrada = "10On20Off30On40="
#somador_on_off(entrada)  # Deve imprimir 70

#entrada = "5On10OffOff20On30Off40On50="
#somador_on_off(entrada)  # Deve imprimir 95

#entrada = "Off10On20Off30On40="
#somador_on_off(entrada)  # Deve imprimir 60

#entrada = "On123abc456OFf789On100="
#somador_on_off(entrada)  # Deve imprimir 679

#entrada = "ON50oN60Off70="
#somador_on_off(entrada)  # Deve imprimir 110
#