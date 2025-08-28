import tarefas #import para chamar as funcoes do programa.

#Programa Principal
while True: 
    print('='*30)
    print('Minha Lista de Tarefas'.center(30))
    print('='*30)

    print("""
    1-Adicionar tarefas
    2-Listar tarefas pedentes
    3-Marcar concluidas
    4-Remover tarefas
    5-Finalizar
        """)
    print('='*30)

   
    escolha = int(input('Escolha uma das opcoes: ')) #variavel para armazenar as escolhas do usuario.

    print()
    if escolha == 1: #se a escolha do usuario foi 1 chamara o metodo para adicionar tarefa.
            tarefas.adicionar() #chamndo a funçao adicionar.
    elif escolha == 2:
            tarefas.listar()
    elif escolha == 3:
            tarefas.concluir()
    elif escolha == 4:
            tarefas.remover()
    elif escolha == 5:
        tarefas.exibir()
        break
print('Saindo da lista...')