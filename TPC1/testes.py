from somador_on_off import somador_on_off

def rodar_testes():
    exemplos = [
        "12abc34On56OfF78On90=",  # Deve imprimir 192
        "10On20Off30On40=",  # Deve imprimir 70
        "5On10OffOff20On30Off40On50=",  # Deve imprimir 95
        "Off10On20Off30On40=",  # Deve imprimir 60
        "On123abc456OFf789On100=",  # Deve imprimir 679
        "ON50oN60Off70="  # Deve imprimir 110
    ]

    print("Escolha uma opção:")
    print("1 - Usar exemplos predefinidos")
    print("2 - Inserir entrada personalizada")
    escolha = input("Opção: ")

    if escolha == "1":
        for entrada in exemplos:
            print(f"Entrada: {entrada}")
            somador_on_off(entrada)
    elif escolha == "2":
        entrada = input("Digite a entrada: ")
        somador_on_off(entrada)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    rodar_testes()