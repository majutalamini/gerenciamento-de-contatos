dicionario = {}

while True:

    print("=== Gerenciador de Contatos ===")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Remover Contato")
    print("4. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha > 5 and escolha <= 0:
        print("Escolha uma numeração de 1 até 4.")
    
    elif escolha == 1:
        print("=== ADICIONAR CONTATO ===")
        nome = str(input("Nome: "))
        telefone = int(input("Telefone: "))
        dicionario[nome] = telefone
        print("Contato adicionado com sucesso!")

    elif escolha == 2:
        if dicionario:
            for nome, telefone in dicionario.items():
                print("=== LISTAR CONTATOS ===")
                print(f"Nome: {nome}, Telefone: {telefone}")
        
        else:
            print("==== LISTAR CONTATOS ====")
            print("Sem contatos cadastrados.")

    elif escolha == 3:
        print("=== REMOVER CONTATO ===")
        remover_contato = str(input("Digite o nome que deseja remover: "))

        if remover_contato in dicionario:
            del dicionario[remover_contato]
            print("Contato removido com sucesso!")
        
        else: 
            print("Este contato não está cadastrado.")
    
    else:
        print("=== SAIR ===")
        print("Você saiu do gerenciador de contatos.")
        break