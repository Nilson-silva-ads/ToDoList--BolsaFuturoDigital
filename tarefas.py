from time import sleep


lista_pendente = []
lista_concluida = []
lista_principal = [lista_pendente, lista_concluida]


def adicionar(): #funcao para adicionar uma tarefa.
    print()
    task = input('''Adicone uma tarefa:
        ''') #input para adicionar a tarefa.
    lista_pendente.append(task) #metodo append que adicionar a tarefa dentro da lista pendente.
    print('tarefa adicionada com sucesso!')
    sleep(1)


def listar(): #funcao para listar as tarefas pendentes.
    print()
    for pos, tarefas in enumerate(lista_pendente):  #usando o for com enumerate para listar todas as tarefas de forma ordenada com seus id.      
        print(f'{pos+1}ª - {tarefas}')
        sleep(1)

def concluir(): #funcao para marcar como concluido uma tarefa da lista pendente.
    id = int(input('Digite o numero da tarefa que deseja marcar como concluida: '))
    lista_concluida.append(lista_pendente[id] ) 
    del lista_pendente[id]
    print(f'tarefa concluida com sucesso!')
    sleep(1)

def remover(): #funcao para remover uma terega da lista.
    id = int(input('Digite o numero da tarefa que deseja Excluir: '))
    del lista_pendente[id]
    print('Tarefa Excluida com sucesso!!')


def exibir(): #funcao para exibir as listas em ordem.
    print('Tarefas pendentes:')
    for pos, tarefas in enumerate(lista_pendente): #for para listar todos os intem da tabela pela sua posiçao.
        print(f'Tarefa{pos+1} : {tarefas}')
    print()
    print('Tarefas Concluidas:')
    for pos, tarefas in enumerate(lista_concluida):# listar todos os itens da lista tarefas concluidas cada um em sua posição.
        print(f'Tarefa{pos+1} : {tarefas}' )
    print()