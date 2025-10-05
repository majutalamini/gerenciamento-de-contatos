lista_afazeres = []

print("=== GERENCIADOR DE TAREFAS ===")
print("1.  Adicionar tarefa")
print("2.  remover tarefa")
print("3.  Listar tarefas")
print("4.  Sair do programa")

escolha = int(input("Opção: "))

while True:
    if escolha == 1:
        adicionar_tarefa = str(input("Qual tarefa deseja adicionar? "))
        adicionar_tarefa = adicionar_tarefa.capitalize
        lista_afazeres.append(adicionar_tarefa)

        if len(lista_afazeres) > 1:

            if adicionar_tarefa in lista_afazeres:
                print("Esta tarefa já foi adicionada anteriormente.")
                break
            else:
                print("Tarefa adicionada com sucesso!")
                break
     
    elif escolha == 2:
        remover_tarefa = str(input("Qual tarefa deseja remover? "))
        lista_afazeres.pop(remover_tarefa)

    elif escolha == 3:
        print(lista_afazeres)
