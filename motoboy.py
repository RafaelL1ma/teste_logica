# Declarando os Dados do teste em dicionários
moto1 = {
    'nome': "Junior",
    'taxa': 2
}
moto2 = {
    'nome': "Felipe",
    'taxa': 2
}
moto3 = {
    'nome': "João",
    'taxa': 2
}
moto4 = {
    'nome': "Nicolas",
    'taxa': 2
}
moto5 = {
    'nome': "Pedro",
    'taxa': 3
}
loja1 = {
    'loja': "loja1",
    'pedido1': 50,
    'pedido2': 50,
    'pedido3': 50,
    'taxa_por_pedido': 0.05
}
loja2 = {
    'loja': "loja2",
    'pedido1': 50,
    'pedido2': 50,
    'pedido3': 50,
    'pedido4': 50,
    'taxa_por_pedido': 0.05
}
loja3 = {
    'loja': "loja3",
    'pedido1': 50,
    'pedido2': 50,
    'pedido3': 100,
    'taxa_por_pedido': 0.15
}

# Estrutura de repetição criada com objetivo manter o programa funcionando após a saida de cada entrada processada
while True:
    print(f"====================MOTOBOYS====================")
    # Exibindo a lista de motoboys disponiveis
    print(
        f"MotoBoys: {moto1['nome']} - {moto2['nome']} - {moto3['nome']} - {moto4['nome']} - {moto5['nome']}"
        "\n Caso deseja sair do programa digite: sair")
    # Input que recebe a entrada de dados do usuário(obs: o lower é para transformar qualquer string recebida em minúsculo)
    motoboy = str(input("Escolha um motoboy: ")).lower()
    # Essa condição retorna caso o usuário não informe nada todos os motoboys com lojas, pedidos e comissões respectivos
    if motoboy == "":
        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto1['taxa'] + loja1['pedido3'] * loja2['taxa_por_pedido']
        comissao2 = moto1['taxa'] + loja2['pedido1'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto1['nome']}====================")

        print(f"Motoboy: {moto1['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja1['loja']} e {loja2['loja']}"
              f"\n Pedidos: {loja1['loja']}: Pedido 3 de R${loja1['pedido3']} | {loja2['loja']}: Pedido 1 de R${loja2['pedido1']}"
              f"\n Comissão da {loja1['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja2['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto2['taxa'] + loja2['pedido3'] * loja2['taxa_por_pedido']
        comissao2 = moto2['taxa'] + loja1['pedido2'] * loja1['taxa_por_pedido']
        comissao3 = moto2['taxa'] + loja3['pedido2'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto2['nome']}====================")

        print(f"Motoboy: {moto2['nome']}"
              f"\n Número de pedidos: 3"
              f"\n Lojas: {loja2['loja']}, {loja1['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 3 de R${loja2['pedido3']} | {loja1['loja']}: Pedido 2 de R${loja1['pedido2']} | {loja3['loja']}: Pedido 2 de R${loja3['pedido2']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja1['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto3['taxa'] + loja2['pedido4'] * loja2['taxa_por_pedido']
        comissao2 = moto3['taxa'] + loja3['pedido3'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto3['nome']}====================")

        print(f"Motoboy: {moto3['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja2['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 4 de R${loja2['pedido4']} | {loja3['loja']}: Pedido 3 de R${loja3['pedido3']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja3['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto4['taxa'] + loja1['pedido1'] * loja1['taxa_por_pedido']
        comissao_total = comissao1

        print(f"===================={moto4['nome']}====================")

        print(f"Motoboy: {moto4['nome']}"
              f"\n Número de pedidos: 1"
              f"\n Lojas: {loja1['loja']}"
              f"\n Pedidos: {loja1['loja']}: Pedido 1 de R${loja1['pedido1']}"
              f"\n Comissão da {loja1['loja']}: R${comissao1:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto5['taxa'] + loja2['pedido2'] * loja2['taxa_por_pedido']
        comissao2 = moto5['taxa'] + loja3['pedido1'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto5['nome']}====================")

        print(f"Motoboy: {moto5['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja2['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 2 de R${loja2['pedido2']} | {loja3['loja']}: Pedido 1 de R${loja3['pedido1']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja3['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")

    # Retorna as informações relacionadas a o motoboy1
    elif motoboy == "junior":

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto1['taxa'] + loja1['pedido3'] * loja2['taxa_por_pedido']
        comissao2 = moto1['taxa'] + loja2['pedido1'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto1['nome']}====================")

        print(f"Motoboy: {moto1['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja1['loja']} e {loja2['loja']}"
              f"\n Pedidos: {loja1['loja']}: Pedido 3 de R${loja1['pedido3']} | {loja2['loja']}: Pedido 1 de R${loja2['pedido1']}"
              f"\n Comissão da {loja1['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja2['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")
    # Retorna as informações relacionadas a o motoboy2
    elif motoboy == "felipe":

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto2['taxa'] + loja2['pedido3'] * loja2['taxa_por_pedido']
        comissao2 = moto2['taxa'] + loja1['pedido2'] * loja1['taxa_por_pedido']
        comissao3 = moto2['taxa'] + loja3['pedido2'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2 + comissao3

        print(f"===================={moto2['nome']}====================")

        print(f"Motoboy: {moto2['nome']}"
              f"\n Número de pedidos: 3"
              f"\n Lojas: {loja2['loja']}, {loja1['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 3 de R${loja2['pedido3']} | {loja1['loja']}: Pedido 2 de R${loja1['pedido2']} | {loja3['loja']}: Pedido 2 de R${loja3['pedido2']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja1['loja']}: R${comissao2:.2f}"
              f"\n Comissão da {loja3['loja']}: R${comissao3:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")
    # Retorna as informações relacionadas a o motoboy3
    elif motoboy == "joão":

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto3['taxa'] + loja2['pedido4'] * loja2['taxa_por_pedido']
        comissao2 = moto3['taxa'] + loja3['pedido3'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto3['nome']}====================")

        print(f"Motoboy: {moto3['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja2['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 4 de R${loja2['pedido4']} | {loja3['loja']}: Pedido 3 de R${loja3['pedido3']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja3['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")
    # Retorna as informações relacionadas a o motoboy4
    elif motoboy == "nicolas":

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto4['taxa'] + loja1['pedido1'] * loja1['taxa_por_pedido']
        comissao_total = comissao1

        print(f"===================={moto4['nome']}====================")

        print(f"Motoboy: {moto4['nome']}"
              f"\n Número de pedidos: 1"
              f"\n Lojas: {loja1['loja']}"
              f"\n Pedidos: {loja1['loja']}: Pedido 1 de R${loja1['pedido1']}"
              f"\n Comissão da {loja1['loja']}: R${comissao1:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")
    # Retorna as informações relacionadas a o motoboy5
    elif motoboy == "pedro":

        # Calculo relacionado a comissão do moto boy em cada pedido de cada loja e sua comissão total que detém a soma do que ganhou em cada pedido
        comissao1 = moto5['taxa'] + loja2['pedido2'] * loja2['taxa_por_pedido']
        comissao2 = moto5['taxa'] + loja3['pedido1'] * loja3['taxa_por_pedido']
        comissao_total = comissao1 + comissao2

        print(f"===================={moto5['nome']}====================")

        print(f"Motoboy: {moto5['nome']}"
              f"\n Número de pedidos: 2"
              f"\n Lojas: {loja2['loja']} e {loja3['loja']}"
              f"\n Pedidos: {loja2['loja']}: Pedido 2 de R${loja2['pedido2']} | {loja3['loja']}: Pedido 1 de R${loja3['pedido1']}"
              f"\n Comissão da {loja2['loja']}: R${comissao1:.2f}"
              f"\n Comissão da {loja3['loja']}: R${comissao2:.2f}"
              f"\n Comissão total: R${comissao_total:.2f}")
    # Condição onde o usuário pode sair do programa caso tenha terminado as consultas
    elif motoboy == "sair":
        print("Até Logo!")
        break
    # Condição que testa se oque foi informado é válido
    else:
        print("Digite somente palavras válidas!")
