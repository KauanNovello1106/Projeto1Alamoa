import os
os.system('cls')

def menu():
    cmd = int(input("""
1 - Comidas e Restaurantes parceiros
2 - Troca de Enxovais (Lençol, Toalhas, Travesseiros, Tapetes...)
3 - Controle dos Dispositivos do Quarto (Tv, Ar-Condicionado, Luz, Cortina)
4 - Informações Turisticas (Locais Próximos, Praias, Parques...)
5 - Informações do Hotel (Eventos, Horários das Refeições)
6 - Serviços adicionais (Parceiros do Hotel: Serviços de Massagem, Passeios de Bug, Fotográfos...)

Digite o número que deseja: """))

    if cmd == 1:
        tela1()
    elif cmd == 2:
        tela2()
    elif cmd == 3:
        tela3()
    elif cmd == 4:
        tela4()
    elif cmd == 5:
        tela5()
    elif cmd == 6:
        tela6()
    else:
        os.system('cls')
        print("Você digitou um comando invalido, digite novamente uma das opções abaixo:")
        menu()

def tela1():
    print('você abriu a tela 1')
def tela2():
    print('você abriu a tela 2')
def tela3():
    print('você abriu a tela 3')
def tela4():
    print('você abriu a tela 4')
def tela5():
    print('você abriu a tela 5')
def tela6():
    print('você abriu a tela 6')

menu()