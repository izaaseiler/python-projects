print(f"\033[1m\033[45m GERADOR DE TAREFAS \033[0m")

def mostrar_menu():
    print("\nOpções disponíveis:")
    print(f"\n\033[35m[1]\033[0m Criar uma tarefa")
    print(f"\033[35m[2]\033[0m Ler as tarefas")
    print(f"\033[35m[3]\033[0m Atualizar tarefa")
    print(f"\033[35m[4]\033[0m Finalizar tarefa")
    print(f"\033[35m[5]\033[0m Excluir tarefa")
    print(f"\033[35m[6]\033[0m Encerrar o programa")

def carregar_tarefas(caminho_arquivo):
    """Carrega as tarefas do arquivo e retorna uma lista com as tarefas existentes."""
    tarefas_existentes = []
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                tarefas_existentes.append(linha.strip())
    except FileNotFoundError:
        return tarefas_existentes
    return tarefas_existentes

def salvar_tarefas(tarefas, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'a') as arquivo:
            for tarefa in tarefas:
                arquivo.write(f"{tarefa}\n")
    except Exception as e:
        pass

caminho_arquivo = 'C:\\Users\\seile\\Projects\\python\\gerador_de_tarefas\\tarefas.txt'

def criar_tarefa(tarefas):
    tarefa = input("Informe a tarefa que deseja criar: ")
    tarefas_existentes = carregar_tarefas(caminho_arquivo)
    
    if tarefa in tarefas_existentes:
        print(f"\033[31mA tarefa já existe em nosso banco de dados!\033[0m")  # Cor vermelha para indicar que a tarefa já existe
        
        # Pergunta ao usuário se ele deseja adicionar a tarefa existente à lista atual
        adicionar_existente = input("Deseja adicionar a tarefa existente à lista atual? (s/n): ").lower()
        if adicionar_existente == 's':
            # Se o usuário responder "sim", adicione a tarefa à lista atual
            if tarefa not in tarefas:
                tarefas.append(tarefa)
                print(f"\033[32mTarefa existente adicionada à lista atual!\033[0m")
        else:
            print("Tarefa não adicionada à lista atual.")
    else:
        # Se a tarefa não existir no arquivo, adicione-a à lista atual e ao arquivo
        tarefas.append(tarefa)
        print("\033[32mTarefa criada com sucesso!\033[0m")  # Cor verde para indicar que a tarefa foi criada
        salvar_tarefas([tarefa], caminho_arquivo)

def ler_tarefas(tarefas):
    print("\nTarefas a fazer:")
    if tarefas:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa pendente.")

def atualizar_tarefa(tarefas):
    if tarefas:
        while True:
            try:
                tarefa_numero = int(input("\nDigite o número da tarefa a ser atualizada: "))
                
                if 1 <= tarefa_numero <= len(tarefas):
                    nova_tarefa = input("Informe a nova descrição para a tarefa: ")
                    tarefas[tarefa_numero - 1] = nova_tarefa
                    print("Tarefa atualizada com sucesso!")
                    salvar_tarefas(tarefas, 'C:\\Users\\seile\\Projects\\python\\gerador_de_tarefas\\tarefas.txt')
                    break
                else:
                    print("Número de tarefa inválido.")
                    
            except ValueError:
                print("Número inválido. Por favor, digite um número válido.")

def finalizar_tarefa(tarefas):
    if tarefas:
        while True:
            try:
                tarefa_numero = int(input("\nDigite o número da tarefa a ser finalizada: "))
                if 1 <= tarefa_numero <= len(tarefas):
                    tarefa_finalizada = tarefas.pop(tarefa_numero - 1)
                    print(f"Tarefa '{tarefa_finalizada}' finalizada com sucesso!")
                    break
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Número inválido. Por favor, digite um número válido.")

def excluir_tarefa(tarefas):
    if tarefas:
        while True:
            try:
                tarefa_numero = int(input("\nDigite o número da tarefa a ser excluída: "))

                if 1 <= tarefa_numero <= len(tarefas):
                    tarefa_excluida = tarefas.pop(tarefa_numero - 1)
                    print(f"Tarefa '{tarefa_excluida}' excluída com sucesso!")
                    break
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Número inválido. Por favor, digite um número válido.")

def encerrar_programa():
    print("Programa encerrado com sucesso.")
    exit()

def main():
    """Função principal que executa o programa."""
    tarefas = []
    while True:
        mostrar_menu()
        escolha = input("\nInforme a opção desejada: ")
        
        if escolha == '1':
            criar_tarefa(tarefas)
        elif escolha == '2':
            ler_tarefas(tarefas)
        elif escolha == '3':
            atualizar_tarefa(tarefas)
        elif escolha == '4':
            finalizar_tarefa(tarefas)
        elif escolha == '5':
            excluir_tarefa(tarefas)
        elif escolha == '6':
            encerrar_programa()
        else:
            print("Opção inválida. Por favor, informe um número válido.")

if __name__ == "__main__":
    main()