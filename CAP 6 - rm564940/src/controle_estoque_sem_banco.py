

import json
from datetime import datetime, timedelta
import os

CAMINHO_JSON = "estoque.json"

def carregar_estoque():
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_estoque(estoque):
    with open(CAMINHO_JSON, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def plural(unidade, quantidade):
    return f"{unidade}s" if quantidade > 1 and not unidade.endswith("s") else unidade

def adicionar_insumo(estoque):
    print('\n--- ADICIONAR INSUMO ---')

    nome = input("Nome do insumo: ").strip()
    fornecedor = input("Fornecedor: ").strip()

    unidade = input("Unidade de medida (saco/kg/litro): ").strip().lower()
    while unidade not in ["saco", "kg", "litro"]:
        print("Unidade inválida. Escolha entre: saco, kg ou litro.")
        unidade = input("Unidade de medida (saco/kg/litro): ").strip().lower()

    while True:
        try:
            quantidade = float(input(f"Quantidade atual em estoque ({unidade}): ").replace(",", "."))
            if quantidade < 0:
                print("A quantidade não pode ser menor que zero.")
            else:
                break
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            consumo = float(input(f"Consumo médio diário ({unidade}): ").replace(",", "."))
            if consumo <= 0:
                print("O consumo deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            lead_time = int(input("Tempo de entrega (em dias): "))
            if lead_time <= 0:
                print("O tempo de entrega deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Digite um número inteiro válido.")

    data_cadastro = datetime.today().date()
    estoque_minimo = consumo * lead_time
    estoque_operacional = quantidade - estoque_minimo
    tempo_estoque_util = estoque_operacional / consumo if consumo != 0 else 0

    if tempo_estoque_util < 0:
        data_aviso = data_cadastro
        print("Atenção: o estoque está abaixo do mínimo. É necessário realizar a compra agora mesmo.")
    else:
        data_aviso = data_cadastro + timedelta(days=tempo_estoque_util)
        print("A próxima compra deve ser feita em:", data_aviso.strftime("%d/%m/%Y"))

    insumo = {
        "nome": nome,
        "fornecedor": fornecedor,
        "unidade": unidade,
        "quantidade": quantidade,
        "consumo": consumo,
        "lead_time": lead_time,
        "estoque_minimo": estoque_minimo,
        "data_cadastro": data_cadastro.strftime("%d/%m/%Y"),
        "data_aviso_compra": data_aviso.strftime("%d/%m/%Y")
    }

    estoque.append(insumo)
    salvar_estoque(estoque)
    print("Insumo cadastrado com sucesso!")

def verificar_estoque():
    estoque = carregar_estoque()
    if not estoque:
        print("\nNenhum insumo cadastrado.")
        return

    print("\n--- Verificação de Estoque ---")
    hoje = datetime.today().date()
    alterado = False

    for insumo in estoque:
        data_cadastro = datetime.strptime(insumo["data_cadastro"], "%d/%m/%Y").date()
        dias_passados = (hoje - data_cadastro).days
        consumo_total = dias_passados * insumo["consumo"]
        nova_quantidade = max(insumo["quantidade"] - consumo_total, 0)
        nova_quantidade = round(nova_quantidade, 2)

        if nova_quantidade != insumo["quantidade"]:
            insumo["quantidade"] = nova_quantidade
            alterado = True

        unidade = plural(insumo['unidade'], nova_quantidade)
        print(f"\nInsumo: {insumo['nome']}")
        print(f"Fornecedor: {insumo['fornecedor']}")
        print(f"Estoque atual: {nova_quantidade} {unidade}")
        print(f"Consumo diário: {insumo['consumo']} {unidade}")
        print(f"Estoque mínimo: {insumo['estoque_minimo']} {unidade}")
        print(f"Data de cadastro: {insumo['data_cadastro']}")
        print(f"Data da próxima compra: {insumo['data_aviso_compra']}")

        data_aviso = datetime.strptime(insumo['data_aviso_compra'], "%d/%m/%Y").date()

        if data_aviso <= hoje:
            if data_aviso < data_cadastro:
                print("Estoque defasado. Realizar a compra imediatamente!")
            else:
                print("Atenção: chegou o dia de realizar o pedido deste insumo.")
        else:
            dias_restantes = (data_aviso - hoje).days
            print(f"Ainda faltam {dias_restantes} dias para realizar um novo pedido.")

    if alterado:
        salvar_estoque(estoque)
        print("\nEstoque atualizado com base no consumo diário. Alterações salvas.")

def editar_insumo(estoque):
    if not estoque:
        print("Nenhum insumo cadastrado.")
        return
    print('\n--- EDITAR INSUMO ---')
    for i, insumo in enumerate(estoque):
        print(f"{i + 1}. {insumo['nome']}")
    print("0. Voltar ao menu de insumos")

    while True:
        try:
            escolha = int(input("\nEscolha o número do insumo que deseja editar: "))
            if escolha == 0:
                print("Voltando ao menu de insumos.")
                return
            elif 1 <= escolha <= len(estoque):
                insumo = estoque[escolha - 1]
                print(f"\nEditando insumo: {insumo['nome']}")

                insumo['nome'] = input("Novo nome do insumo: ").strip()
                insumo['fornecedor'] = input("Novo fornecedor: ").strip()

                unidade = input("Nova unidade de medida (saco/kg/litro): ").strip().lower()
                while unidade not in ["saco", "kg", "litro"]:
                    print("Unidade inválida. Escolha entre: saco, kg ou litro.")
                    unidade = input("Nova unidade de medida (saco/kg/litro): ").strip().lower()
                insumo['unidade'] = unidade

                while True:
                    try:
                        insumo['quantidade'] = float(input(f"Nova quantidade em estoque ({unidade}): ").replace(",", "."))
                        if insumo['quantidade'] < 0:
                            print("A quantidade não pode ser menor que zero.")
                        else:
                            break
                    except ValueError:
                        print("Digite um número válido.")

                while True:
                    try:
                        insumo['consumo'] = float(input(f"Novo consumo médio diário ({unidade}): ").replace(",", "."))
                        if insumo['consumo'] <= 0:
                            print("O consumo deve ser maior que zero.")
                        else:
                            break
                    except ValueError:
                        print("Digite um número válido.")

                while True:
                    try:
                        insumo['lead_time'] = int(input("Novo tempo de entrega (em dias): "))
                        if insumo['lead_time'] <= 0:
                            print("O tempo deve ser maior que zero.")
                        else:
                            break
                    except ValueError:
                        print("Digite um número válido.")

                data_cadastro = datetime.today().date()
                estoque_minimo = insumo['consumo'] * insumo['lead_time']
                estoque_operacional = insumo['quantidade'] - estoque_minimo
                tempo_estoque_util = estoque_operacional / insumo['consumo'] if insumo['consumo'] != 0 else 0

                data_aviso = data_cadastro if tempo_estoque_util < 0 else data_cadastro + timedelta(days=tempo_estoque_util)

                insumo['estoque_minimo'] = estoque_minimo
                insumo['data_cadastro'] = data_cadastro.strftime("%d/%m/%Y")
                insumo['data_aviso_compra'] = data_aviso.strftime("%d/%m/%Y")

                salvar_estoque(estoque)
                print("Insumo atualizado com sucesso.")
                return
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Digite um número válido.")

def remover_insumo(estoque):
    if not estoque:
        print("Nenhum insumo cadastrado.")
        return

    print('\n--- REMOVER INSUMO ---')
    for i, insumo in enumerate(estoque):
        print(f"{i + 1}. {insumo['nome']}")
    print("0. Voltar ao menu de insumos")

    while True:
        try:
            escolha = int(input("\nEscolha o número do insumo que deseja remover: "))
            if escolha == 0:
                print("Voltando ao menu de insumos.")
                return
            elif 1 <= escolha <= len(estoque):
                removido = estoque.pop(escolha - 1)
                salvar_estoque(estoque)
                print(f"Insumo '{removido['nome']}' removido com sucesso.")
                return
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Digite um número válido.")

def menu_controle_insumos(estoque):
    while True:
        print("\n--- CONTROLE DE INSUMOS ---")
        print("1. Adicionar insumo")
        print("2. Editar insumo")
        print("3. Remover insumo")
        print("4. Voltar ao menu principal")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_insumo(estoque)
        elif opcao == "2":
            editar_insumo(estoque)
        elif opcao == "3":
            remover_insumo(estoque)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def menu():
    estoque = carregar_estoque()
    while True:
        print("\n==== CONTROLE DE ESTOQUE ====")
        print("1. Controle de insumos")
        print("2. Verificar estoque")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_controle_insumos(estoque)
        elif opcao == "2":
            verificar_estoque()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

menu()


'''
#SUGESTÕES DE APRIMORAMENTO FUTURO
    - MANDAR MENSAGEM PARA O USUÁRIO AVISANDO QUE CHEGOU O DIA DA COMPRA;
    - CONTROLE DE CONSUMO DE ESTOQUE AUTOMATIZADO (USO DE SENSORES/ CÓDIGO DE BARRAS)
    - COMPRAR INSUMOS COM UM CLIQUE
    
    





























from datetime import datetime, timedelta
import os

consumo_medio = int(input("Consumo médio diário: "))
lead_time = int(input("Tempo de entrega (em dias): "))
quantidade_atual = int(input("Quantidade atual em estoque: "))

data_cadastro = datetime.today().date()
estoque_minimo = consumo_medio * lead_time

estoque_operacional = quantidade_atual - estoque_minimo
tempo_estoque_util = (estoque_operacional * 1)/consumo_medio


data_aviso_compra = data_cadastro + timedelta(days=tempo_estoque_util)


print('consumo medio',consumo_medio)
print('lead time',lead_time)
print('quantidade atual',quantidade_atual)

print('data cadastro', data_cadastro)
print('estoque mínimo',estoque_minimo)
print('dias para o pedido', tempo_estoque_util)
print('data aviso compra',data_aviso_compra)

'''