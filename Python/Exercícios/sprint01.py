import datetime

def calcular_valor(horas):
    # calcular o valor a ser pago com base no tempo de permanência
    if horas <= 3:
        return 5
    else:
        return 5 + (horas - 3) * 2

registros = []

while True:
    # exibir menu de opções
    print("Selecione uma opção:")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Ver registros")
    print("4 - Sair")

    opcao = input("Opção selecionada: ")

    if opcao == "1":
        # registrar entrada de veículo
        placa = input("Digite a placa do veículo: ")
        entrada = datetime.datetime.now()
        registro = {"placa": placa, "entrada": entrada}
        registros.append(registro)
        print("Entrada registrada com sucesso.")

    elif opcao == "2":
        # registrar saída de veículo e calcular valor a ser pago
        placa = input("Digite a placa do veículo: ")
        for registro in registros:
            if registro["placa"] == placa:
                saida = datetime.datetime.now()
                horas = (saida - registro["entrada"]).total_seconds() / 3600
                valor = calcular_valor(horas)
                registro["saida"] = saida
                registro["valor"] = valor
                print(f"Saída registrada com sucesso. Valor a ser pago: R$ {valor:.2f}")
                break
        else:
            print("Placa não encontrada nos registros.")

    elif opcao == "3":
        # exibir todos os registros
        for registro in registros:
            placa = registro["placa"]
            entrada = registro["entrada"].strftime("%d/%m/%Y %H:%M:%S")
            saida = registro.get("saida", "-")
            if saida == "-":
                horas = "-"
                valor = "-"
            else:
                horas = (saida - registro["entrada"]).total_seconds() / 3600
                valor = registro["valor"]
            print(f"Placa: {placa} | Entrada: {entrada} | Saída: {saida} | Horas: {horas:.2f} | Valor: R$ {valor:.2f}")

    elif opcao == "4":
        # sair do programa
        break

    else:
        print("Opção inválida.")