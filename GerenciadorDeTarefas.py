# estrutura das tarefas
# tarefas = [{id: int
#             prioridade: 1 ou 2 ou 3
#             concluida: True ou False
#             descricao: str}]

import csv

# definir funções

def validar_entrada_numerica(valor_min, valor_max, pergunta):
    while True:
        try:
            valor = int(input(pergunta))
            if valor_min <= valor <= valor_max:
                return valor
            else:
                print("Por favor, insira um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def buscar_tarefa_por_id(lista_tarefas):
    tarefa_id = validar_entrada_numerica(1,max((tarefa['id'] for tarefa in lista_tarefas), default=0), "\nDigite o ID da tarefa: ")
    for tarefa in lista_tarefas:
        if tarefa['id'] == tarefa_id:
            return tarefa
    return None

def carregar_tarefas(lista_tarefas):
    try:
        with open('tarefas.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tarefa = {
                    'id': int(row['id']),
                    'prioridade': int(row['prioridade']),
                    'concluida': (row['concluida'] == 'True'),
                    'descricao': row['descricao']
                }
                lista_tarefas.append(tarefa)
        print("\nTarefas carregadas com sucesso!\n")
    except FileNotFoundError:
        print("\nArquivo de tarefas não encontrado. Iniciando com uma lista vazia.\n")

def exibir_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("\nNão há tarefas para exibir.\n")
        return

    tarefas_ordenadas = sorted(lista_tarefas, key=lambda tarefa: tarefa['prioridade'])
    
    for tarefa in tarefas_ordenadas:
        print(f"\nID: {tarefa['id']} | Prioridade: {tarefa['prioridade']} | Descrição: {tarefa['descricao']} | Concluída: {'[x]' if tarefa['concluida'] else '[ ]'}")
    print("\n----------------------------------------------------------------------------\n")

def adicionar_tarefa(lista_tarefas):
    # Gerar um novo ID para a tarefa (maior ID já existente + 1)
    novo_id = max((tarefa['id'] for tarefa in lista_tarefas), default=0) + 1
    nova_prioridade = validar_entrada_numerica(1, 3, "\nDigite a prioridade da nova tarefa (1 = Alta, 2 = Média, 3 = Sem prioridade): ")
    nova_descricao = input("\nDigite a descrição da nova tarefa: ")

    nova_tarefa = {
                    'id': novo_id,
                    'prioridade': nova_prioridade,
                    'concluida': False,
                    'descricao': nova_descricao
    }

    lista_tarefas.append(nova_tarefa)

    print(f"\nID: {nova_tarefa['id']} | Prioridade: {nova_tarefa['prioridade']} | Descrição: {nova_tarefa['descricao']} | Concluída: [ ]")
    print("\nTarefa adicionada com sucesso!")
    print("\n----------------------------------------------------------------------------\n")

def concluir_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("\nNão há tarefas cadastradas.\n")
        return
    
    tarefa = buscar_tarefa_por_id(lista_tarefas)
    
    if tarefa is None:
        print("\nTarefa não encontrada.\n")
        return
    
    tarefa['concluida'] = True
    print('\nTarefa concluída com sucesso!')
    print("\n----------------------------------------------------------------------------\n")

def editar_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("\nNão há tarefas cadastradas.\n")
        return
    
    tarefa = buscar_tarefa_por_id(lista_tarefas)
    
    if tarefa is None:
        print("\nTarefa não encontrada.\n")
        return
        
    opcao_editado = validar_entrada_numerica(1, 2, "\nO que voce gostaria de editar? (1 - Descrição, 2 - Prioridade)\nResposta:")
    
    if opcao_editado == 1:
        nova_descricao = input("\nDigite a nova descrição da tarefa: ")
        tarefa['descricao'] = nova_descricao
        print("\nDescrição da tarefa editada com sucesso!")
        print("\n----------------------------------------------------------------------------\n")
    else:
        nova_prioridade = validar_entrada_numerica(1, 3, "\nDigite a nova prioridade da tarefa (1 = Alta, 2 = Média, 3 = Sem prioridade): ")
        tarefa['prioridade'] = nova_prioridade
        print("\nPrioridade da tarefa editada com sucesso!")
        print("\n----------------------------------------------------------------------------\n")

def deletar_tarefa(lista_tarefas):
    if not lista_tarefas:
        print("\nNão há tarefas cadastradas.")
        return
    
    tarefa = buscar_tarefa_por_id(lista_tarefas)
    
    if tarefa is None:
        print("\nTarefa não encontrada.")
        return

    lista_tarefas.remove(tarefa)
    print("\nTarefa deletada com sucesso!")
    print("\n----------------------------------------------------------------------------\n")

def salvar_tarefas(lista_tarefas):
    with open('tarefas.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'prioridade', 'concluida', 'descricao']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lista_tarefas)

# inicio do main

def main():
    tarefas = []

    print("\n=============================== Gerenciador de Tarefas ==============================\n")

    carregar_tarefas(tarefas)

    while True:

        escolha = validar_entrada_numerica(1,6, "\nO que você deseja fazer?\n\n1 - Exibir tarefas\n2 - Adicionar tarefa\n3 - Concluir tarefa\n4 - Editar tarefa\n5 - Deletar tarefa\n6 - Sair\n\nEscolha: ")

        match escolha:
            case 1:
                exibir_tarefas(tarefas)
            case 2:
                adicionar_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case 3:
                concluir_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case 4:
                editar_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case 5:
                deletar_tarefa(tarefas)
                salvar_tarefas(tarefas)
            case 6:
                salvar_tarefas(tarefas)
                print("Tarefas salvas com sucesso!")
                print("\n----------------------------------------------------------------------------\n")
                print("Saindo do programa...")
                break

if __name__ == "__main__":
    main()