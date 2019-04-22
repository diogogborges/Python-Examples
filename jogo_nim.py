def computador_escolhe_jogada(n, m):
    pecas_c = 0
    if n <= m:
        return n
    else:
        pecas_c = n % (m + 1)
        if pecas_c > 0:
            return pecas_c
        else:
            return m
            
def usuario_escolhe_jogada(n, m):
    pecas_u = int(input("Quantas peças você irá tirar? "))
    while pecas_u <= 0:
        print("Jogada inválida, é necessário tirar ao menos 1 peça!")
        pecas_u = int(input("Quantas peças você irá tirar? "))
    while pecas_u > m:
        print("Jogada inválida, não é possível tirar mais peças que o limite.")
        pecas_u = int(input("Quantas peças você irá tirar? "))
    return pecas_u
    
def partida():
    n = int(input("Digite o número de peças: "))
    m = int(input("Digite o limite de peças por rodada: "))
    computador = False
    
    if n % (m + 1) == 0:
        computador = False
        print("Você começa!")
    else:
        computador = True
        print("Computador começa!")
        
    while n > 0:
        
        if computador == False:
            num_pecas = usuario_escolhe_jogada(n, m)
            if num_pecas == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",num_pecas,"peças.")
            computador = True
        else:
            num_pecas = computador_escolhe_jogada(n, m)
            if num_pecas == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",num_pecas,"peças.")
            computador = False
                
        n = n - num_pecas
        print("Peças restantes no tabuleiro:", n)
        
    if computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

def campeonato():
    partidas = 1
    contador_c = 0
    contador_u = 0
    
    while partidas <= 3:
        partida()

        if computador:
            contador_u = contador_u + 1
            print("Você ganhou!")
        else:
            contador_c = contador_c + 1
            print("O computador ganhou!")
            
        partidas = partidas + 1

    print("Placar: Você",contador_u,"X",contador_c,"Computador")
            
print("Bem-vindo ao jogo do NIM! Escolha: ")
print()
print("1 - para jogar uma partida isolada")
modo = int(input("2 - para jogar um campeonato "))

while modo > 2:
    modo = int(input("1 - partida isolada ou 2 - campeonato"))
if modo == 1:
    print("Você escolheu partida isolada!")
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()
        
    
