# Importa as bibliotecas
from random import randint
from time import sleep
from numpy import sqrt


def modulo(x):
    return sqrt(x ** 2)


def int_input():
    while True:
        try:
            var = int(input('Digite aqui:'))
            return var
        except ValueError:
            print('\33[31mValor inválido, tente novamente!\33[m')


tarefas = []  # Armazena as informaçoões de tarefas
pessoas = []  # Armazena temporáriamente as informações de cada pessoa
tarefas_atribuidas = []  # Registra quais tarefas ja foram atribuidas
tarefas_analisadas = []  # Registra quais tarefas foram analizadas
soma_pesos = peso_medio = menor_dif = temp_tar_men_peso = count = temp_dif = temp_tar = o1_1 = o2_1 = 0

# Corpo Principal
while True:
    print('''O que deseja fazer?

    5 - Visualizar Registros e Divisões
    4 - Adicionar e Remover Registros
    3 - Alterar Registros
    2 - Redividir Tarefas
    1 - Dividir Tarefas
    0 - Encerrar o programa
    ''')  # Looby do Programa

    o1 = int(input('Digite aqui: '))

    # Distribui ou Redistribui as Tarefas
    if o1 in [1, 2]:
        # Limpa os valores registrados para atribuir tarefas novamente
        if o1 == 2:
            for p in pessoas:
                p['Tarefas'].clear()
                p['Peso das Tarefas'] = 0
                tarefas_atribuidas.clear()

        # Registra as tarefas e pessoas
        if o1 == 1:
            # Recebe e registra a quantidade de tarefas
            qnt_tarefas = int(input('Informe a quantidade de tarefas: '))

            # Recebe as informações de nome e peso das tarefas
            for i in range(qnt_tarefas):
                tarefas.append({'Nome': str(input(f'Informe o nome da {i + 1}° tarefa: ')),
                                'Peso': int(input(f'Informe o peso dessa {i + 1}° tarefa: '))}.copy())
                soma_pesos += tarefas[i]['Peso']

            # Imprime na tela as terafas registradas
            print()
            print('-' * 50, f'\n{"Tarefas Registradas":^50}'), print('-' * 50)
            for t in tarefas:
                print(f'Nome: {t["Nome"]}; Peso: {t["Peso"]}')
            print('-' * 50)
            print()

            # Recebe e Registra a quantidade de pessoas
            qnt_pessoas = int(input('Informe a quantidade de pessoas: '))
            for o in range(qnt_pessoas):
                pessoas.append({'Nome': str(input(f'Informe o nome da {o + 1}° pessoa: ')),
                                'Tarefas': [],
                                'Peso das Tarefas': 0})

            # Imprime na tela as pessoas registradas
            print()
            print('-' * 50, f'\n{"Pessoas Registradas":^50}'), print('-' * 50)
            for p in pessoas:
                print(f'Nome: {p["Nome"]}')
            print('-' * 50)
            print()

            # Calcula o peso medio ideal para ser atribuido as pessoas
            peso_medio = soma_pesos / len(pessoas)
            print(f'Peso médio: {peso_medio}')

            # Oferece ao utilizador a opção de visualizar as operações do divisor
            o1_1 = str(input('Deseja visualizar as atribuições [S/N]? '))

        # Loop 1 - Divide as tarefas entre as pessoas registradas, uma por uma
        for p in pessoas:
            # Loop 2 - Analisa todas as tarefas e atribui aquelas que somadas ficam mais proxímas do peso medio
            # for i in range(len(tarefas)):
            while len(tarefas_analisadas) < (len(tarefas) - len(tarefas_atribuidas)):
                # Escolhe aleatoriamente uma tarefa
                ind_tar = randint(0, len(tarefas) - 1)

                # Loop 3 - Impede que uma tarefa já escolhida seja atribuida novamente
                while ind_tar in tarefas_analisadas or ind_tar in tarefas_atribuidas:
                    if o1_1 in 'Ss':
                        print(f'Alterando tarefa {tarefas[ind_tar]["Nome"]} ', end='')
                    ind_tar = randint(0, len(tarefas) - 1)
                    if o1_1 in 'Ss':
                        print(f'para {tarefas[ind_tar]["Nome"]}...'), sleep(3)

                temp_tar = tarefas[ind_tar].copy()

                # Mostra que a tarefa pode ser analisada
                if o1_1 in 'Ss':
                    print(f'Analisando tarefa {temp_tar["Nome"]}...'), sleep(3)

                # Atribui uma tarefa se manter o peso abaixo da media
                if p['Peso das Tarefas'] + temp_tar['Peso'] <= peso_medio:
                    p['Tarefas'].append(temp_tar['Nome'])
                    p['Peso das Tarefas'] += temp_tar['Peso']
                    tarefas_atribuidas.append(ind_tar)

                    # Mostra que a tarefa foi atribuida a pessoa
                    if o1_1 in 'Ss':
                        print(f'Tarefa {temp_tar["Nome"]} atribuida a {p["Nome"]}.'), sleep(3)

                # Atribui uma tarefa se aproximar o peso pessoal do peso medio (Sempre vai ocorrer quando uma tarefa
                # com peso maior que o peso_medio estiver sendo executada)
                else:
                    dif = modulo(peso_medio - p['Peso das Tarefas'])

                    if o1_1 in 'Ss':  # Mostra passagem de teste
                        print('pass test 1'), sleep(2)

                    # Loop 4 - Analisa e atribui tarefas a pessoa caso fique mais proxima do limite de peso
                    for pos, t in enumerate(tarefas):
                        if pos not in tarefas_atribuidas:

                            if o1_1 in 'Ss':  # Mostra passagem de teste
                                print('pass test 2'), sleep(2)

                            if count == 0:

                                if o1_1 in 'Ss':  # Mostra passagem de teste
                                    print('pass test 3'), sleep(2)

                                menor_dif = (p['Peso das Tarefas'] + t['Peso']) - peso_medio
                                count += 1
                            else:
                                if (p['Peso das Tarefas'] + t['Peso']) - peso_medio < menor_dif:

                                    if o1_1 in 'Ss':  # Mostra passagem de teste
                                        print('pass test 4'), sleep(2)

                                    menor_dif = (p['Peso das Tarefas'] + t['Peso']) - peso_medio
                                    temp_tar_men_peso = t.copy()

                    # Atribui a tarefa analizada com menor peso
                    if temp_tar_men_peso != 0:

                        if o1_1 in 'Ss':  # Mostra passagem de teste
                            print('pass test 5'), sleep(2)

                        p['Tarefas'].append(temp_tar_men_peso['Nome'])
                        p['Peso das Tarefas'] += temp_tar_men_peso['Peso']
                        tarefas_atribuidas.append(tarefas.index(temp_tar_men_peso))

                temp_tar.clear()
                tarefas_analisadas.append(ind_tar)

                # Mostra as tarefas analizadas
                if o1_1 in 'Ss':
                    print('Tarefas Analisadas:', tarefas_analisadas), sleep(3)

            tarefas_analisadas.clear()
            count = 0

            if o1_1 in 'Ss':
                print(f'Pessoa {p["Nome"]} analisada.'), sleep(3)
                print(f'Tarefas atribuidas a ela: {p["Tarefas"]}'), sleep(3)
                print('')

        # Imprime na tela as divisões de tarefas
        print('-' * 50, f'\n{"Divisão das Tarefas":^50}'), print('-' * 50)

        for pos, p in enumerate(pessoas):
            print(f'Nome: {p["Nome"]}'), print('Tarefas:', end=' ')

            for t in p["Tarefas"]:
                print(t, end=', ')

            print(f'\nPeso Total: {p["Peso das Tarefas"]}\n')

        print('-' * 50)

    # Encerra o programa
    elif o1 == 0:
        print('Encerrando o programa...')
        sleep(1)
        print('Programa Encerrado')
        break

    # Altera os Registros
    elif o1 == 3:
        # Mostra o menu de opções
        print('''
    Que campo deseja alterar?
    1 - Tarefas
    2 - Pessoas
        ''')

        # Recebe a decisão do usuário
        o2 = int(input('Digite aqui: '))

        # Altera os dados das tarefas
        if o2 == 1:
            # Mostra as tarefas registradas e seus pesos
            print('-' * 50, f'\n{"Tarefas Registradas":^50}'), print('-' * 50)
            print(f'{"Cód":<5}{"Nome":<40}{"Peso":<5}')

            for pos, t in enumerate(tarefas):
                print(f'{pos:<5}{t["Nome"]:<40}{t["Peso"]:<5}')

            print('-' * 50)

            o2_1 = int(input('Qual deseja alterar? '))

            # Menu da opções
            print('''
    O que deseja alterar?
    1 - Nome
    2 - Peso
        ''')

            o2_2 = int(input('Digite aqui: '))

            # Recebe um novo nome
            if o2_2 == 1:
                tarefas[o2_1]["Nome"] = str(input('Digite o novo nome: '))

            # Recebe um novo peso
            elif o2_2 == 2:
                tarefas[o2_1]["Peso"] = int(input('Digite o novo peso: '))

            # Imprime aviso de comando inválido
            else:
                print('Comando inválido, tente novamente.')

        # Altera os dados das pessoas
        elif o2 == 2:
            # Imprime na tela as pessoas registradas
            print('-' * 50, f'\n{"Pessoas Registradas":^50}'), print('-' * 50)
            print(f'{"Cód":<5}{"Nome":<45}')

            for pos, p in enumerate(pessoas):
                print(f'{pos:<5}{p["Nome"]:<45}')

            print('-' * 50)

            o2_2_1 = int(input('Qual pessoa deseja alterar? '))

            pessoas[o2_2_1]["Nome"] = str(input('Digite o novo nome: '))
            print()

    # Adiciona e Remove Registros
    elif o1 == 4:
        # Lobby da sessão
        print('''
    O que deseja fazer?    
    1 - Adicionar Registros
    2 - Remover Registros
    ''')

        o4 = int(input('Digite aqui: '))

        # Adiciona Registros
        if o4 == 1:
            # Lobby da sessão Adicionar
            print('''
    Qual campo deseja adicionar registros?
    1 - Tarefas
    2 - Pessoas        
            ''')
            o4_1 = int(input('Digite aqui: '))

            # Adiciona registros de tarefas
            if o4_1 == 1:
                qnt_reg = int(input('Informe a quantidade de registros: '))

                for i in range(qnt_reg):
                    tarefas.append({'Nome': str(input('Nome: ')),
                                    'Peso': int(input('Peso: '))})

            # Adiciona registros de pessoas
            elif o4_1 == 2:
                qnt_reg = int(input('Informe a quantidade de registros: '))

                for i in range(qnt_reg):
                    pessoas.append({'Nome': str(input('Nome: ')),
                                    'Tarefas': [],
                                    'Peso das Tarefas': 0})

        # Remove Registros
        elif o4 == 2:
            # Lobby da Sessão
            print('''
    O que deseja remover?
    1 - Tarefas
    2 - Pessoas
            ''')

            o4_2 = int_input()

            # Remove registros de tarefas
            if o4_2 == 1:
                # Mostra as terefas registradas
                print('-' * 50, f'\n{"Tarefas Registradas":^50}'), print('-' * 50)
                print(f'{"Cód":<5}{"Nome":<40}{"Peso":<5}')
                for pos, t in enumerate(tarefas):
                    print(f'{pos:<5}{t["Nome"]:<40}{t["Peso"]:<5}')
                print('-' * 50)

                o4_2_1_1 = int_input()

                tarefas.pop(o4_2_1_1)

            # Remove registros de pessoas
            elif o4_2 == 2:
                # Imprime na tela as pessoas registradas
                print('-' * 50, f'\n{"Pessoas Registradas":^50}'), print('-' * 50)
                print(f'{"Cód":<5}{"Nome":<45}')
                for pos, p in enumerate(pessoas):
                    print(f'{pos:<5}{p["Nome"]:<45}')
                print('-' * 50)

                o4_2_1 = int_input()

                pessoas.pop(o4_2_1)

    # Visualiza os registros
    elif o1 == 5:
        print()
        print('-' * 50, f'\n{"Tarefas Registradas":^50}'), print('-' * 50)
        for t in tarefas:
            print(f'Nome: {t["Nome"]}; Peso: {t["Peso"]}')
        print('-' * 50)
        print()
        print('-' * 50, f'\n{"Pessoas Registradas":^50}'), print('-' * 50)
        for p in pessoas:
            print(f'Nome: {p["Nome"]}')
        print('-' * 50)
        print()

    # Informa comando inválido
    else:
        print('Comando inválido. Tente novamente.')
