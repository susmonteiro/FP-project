#92560, Susana Monteiro

#variaveis globais (constantes, ja que nao sao alteradas ao longo do codigo)
#facilitam a leitura e interpretacao
INATIVO = 0
ATIVO = 1
INCERTO = -1
STR_INCERTO = 'x'   #o carater x corresponde a representacao externa do estado incerto
POSSIBILIDADES_CELULA = (1,0,-1)    #os valores de estado de uma celula, que podem apenas ser 0, 1 ou -1
POSSIBILIDADES_COORDENADA = (0,1,2) #indice da linha ou coluna possiveis 


#CELULA

def cria_celula(v):
    """cria_celula: {1,0,-1} -> celula
    Recebe um numero (1, 0 ou -1} e devolve a celula (representada por um dicionario) com o respetivo estado"""    
    if v in POSSIBILIDADES_CELULA: #se o valor do estado for 1, 0 ou -1 a celula e criada. Caso contrario, gera um erro
        return {'estado': v}       #a representacao interna da celula e um dicionario, com uma unica entrada, a qual corresponde o valor do seu estado: 1, 0 ou -1
    raise ValueError ('cria_celula: argumento invalido.')

def obter_valor(c):
    """obter_valor: celula -> {1,0,-1}
    Recebe uma celula e devolve o seu estado. Neste caso o estado da celula e o valor associado a entrada estado"""
    return c['estado']

def inverte_estado(c):
    """inverte_estado: celula -> celula
    Recebe uma celula, devolve uma celula com um novo valor de estado"""
    if obter_valor(c) != INCERTO:   #compara o estado da celula com -1
        c['estado'] = abs(obter_valor(c) - 1)   #se o estado da celula for 0 troca para 1 e vice-versa
    return c    #se oestado da celula for -1, mantem -1 

def eh_celula(arg):
    """eh_celula: universal -> logico
    Devolve verdadeiro se corresponder a representacao interna da celula escolhida. False em caso contrario"""
    return isinstance(arg,dict) and len(arg) == 1 and \
           'estado' in arg and obter_valor(arg) in POSSIBILIDADES_CELULA

def celulas_iguais(c1,c2):
    """celulas_iguais: celula x celula -> logico
    Compara duas celulas e, se ambas corresponderem a representacao interna escolhida para celula e forem iguais, devolve True. Caso contrario, devolve False"""
    return eh_celula(c1) and eh_celula(c2) and c1 == c2

def celula_para_str(c):
    """celula_para_str: celula -> cadeia de caracteres 
    Recebe uma celula e devolve a sua representacao externa"""
    if obter_valor(c) == INCERTO:
        return STR_INCERTO      #se a celula tiver o valor de -1, entao a sua representacao externa e 'x'
    return str(obter_valor(c))  #se a celula tiver o valor de 0 ou 1, a sua representacao externa e respetivamente '0' e '1'


#COORDENADA

def cria_coordenada(l,c):
    """cria_coordenada: int x int -> coordenada
    Recebe dois numeros inteiros (pertencentes ao conjunto {0,1,2}) e devolve a coordenada (representada por um tuplo), onde o primeiro argumento corresponde a linha e o segundo a coluna."""
    if l in POSSIBILIDADES_COORDENADA and c in POSSIBILIDADES_COORDENADA\
       and not (l == 2 and c == 0): #se l e c sao 0, 1 ou 2, entao ja sao necessariamente numeros inteiros
        #como a coordenada (2,0) nao existe, e necessario avaliar se os valores inseridos correspondem a esse caso
        return (l,c)
    raise ValueError ('cria_coordenada: argumentos invalidos.')

def coordenada_linha(c):
    """coordenada_linha: coordenada -> int
    Recebe uma coordenada e devolve a sua linha (o primeiro elemento do tuplo)"""
    return c[0]

def coordenada_coluna(c):
    """coordenada_coluna: coordenada -> int
    Recebe uma coordenada e devolve a sua coluna (o segundo elemento do tuplo)"""
    return c[1]

def eh_coordenada(arg):
    """eh_coordenada: universal -> logico
    Devolve verdadeiro se corresponder a representacao interna da coordenada escolhida. False em caso contrario"""    
    return isinstance(arg,tuple) and len(arg) == 2\
           and coordenada_linha(arg) in POSSIBILIDADES_COORDENADA\
           and coordenada_coluna(arg) in POSSIBILIDADES_COORDENADA\
           and arg != (2,0)

def coordenadas_iguais(c1,c2):
    """coordenadas_iguais: coordenada x coordenada -> logico
    Compara duas coordenadas e, se ambas corresponderem a representacao interna escolhida para coordenada e forem iguais, devolve True. Caso contrario, devolve False"""
    return eh_coordenada(c1) and eh_coordenada(c2) and c1 == c2

def coordenada_para_str(c):
    """coordenada_para_str: coordenada -> cadeia de caracteres 
    Recebe uma coordenada e devolve a sua representacao externa"""    
    return '(' + str(coordenada_linha(c)) + ', ' \
           + str(coordenada_coluna(c)) + ')'

#TABULEIRO

def tabuleiro_inicial():
    """tabuleiro_inicial: {} -> tabuleiro
    Devolve o tabuleiro inicial do jogo"""
    return {cria_coordenada(0,0):cria_celula(-1), \
            cria_coordenada(0,1): cria_celula(-1),\
            cria_coordenada(0,2): cria_celula(-1),\
            cria_coordenada(1,0): cria_celula(0), \
            cria_coordenada(1,1): cria_celula(0), \
            cria_coordenada(1,2): cria_celula(-1),\
            cria_coordenada(2,1): cria_celula(0), \
            cria_coordenada(2,2): cria_celula(-1)}

def str_para_tabuleiro(s):
    """str_para_tabuleiro: cadeia de caracteres -> tabuleiro
    Recebe uma string que representa um tabuleiro e devolve a sua representacao interna escolhida (dicionario, cujas chaves sao as coordenadas e os valores associados sao o estado da respetiva celula"""
    if isinstance(s,str) and eh_tuplo_tabuleiro(eval(s)):
        t = transforma_tabuleiro(eval(s))   #transforma o tuplo constituido por 3 tuplos num unico tuplo, onde os elementos se encontram pela mesma ordem 
        return {cria_coordenada(0,0):cria_celula(t[0]), \
                cria_coordenada(0,1): cria_celula(t[1]),\
                cria_coordenada(0,2): cria_celula(t[2]),\
                cria_coordenada(1,0): cria_celula(t[3]), \
                cria_coordenada(1,1): cria_celula(t[4]), \
                cria_coordenada(1,2): cria_celula(t[5]),\
                cria_coordenada(2,1): cria_celula(t[6]), \
                cria_coordenada(2,2): cria_celula(t[7])}        
    #devolve o dicionario cujas chaves sao as coordenadas do tabuleiro, as quais estao associados os elementos da cadeia de caracteres inserida
    raise ValueError ('str_para_tabuleiro: argumento invalido.')

def eh_tuplo_tabuleiro(tab):
    """eh_tuplo_tabuleiro: universal -> logico 
    Verifica se o argumento e um tabuleiro valido, na forma em que deve ser inserido pelo jogador: um tuplo, constituido por 3, os dois primeiros com 3 elementos e o ultimo com 2 elementos"""
    if not (isinstance(tab,tuple) and len(tab) == 3): #verifica se o argumento e um tuplo com 3 elementos
        return False
    for i in range(len(tab)):
        if not isinstance(tab[i],tuple):    #verifica se todos os elementos do tuplo sao tuplos
            return False
        if not ((i == 2 and len(tab[i]) == 2) or \
                ((i == 0 or i == 1) and len(tab[i]) == 3)):  #verifica as dimensoes dos tuplos que constituem o tabuleiro
            return False
        for l in tab[i]:
            if l not in POSSIBILIDADES_CELULA: #verifica se todos os elementos do tuplo sao 0, 1 ou -1
                return False
    return True 

def transforma_tabuleiro(t):
    """transforma_tabuleiro: tuplo -> tuplo
    Recebe um tuplo na forma ((a,b,c),(d,e,f),(g,h)) e devolve o tuplo (a,b,c,d,e,f,g,h)"""
    novo_t = ()
    for tuplo in t:
        for elemento in tuplo:
            novo_t = novo_t + (elemento,)
    return novo_t

def tabuleiro_dimensao(t):
    """tabuleiro_dimensao: tabuleiro -> int
    Devolve o numero de linhas (=numero de colunas) existente no tabuleiro"""
    if eh_tabuleiro(t):
        tuplo_rascunho = () #tuplo que guarda quais as linhas que ja foram contadas para a dimensao
        n_linhas = 0        #numero de linhas contadas  
        for i in t:
            if coordenada_linha(i) not in tuplo_rascunho:   #avalia se a linha atual ainda nao foi contabilizada
                tuplo_rascunho = tuplo_rascunho + (coordenada_linha(i),)    #junta o numero dessa linha ao tuplo_rascunho
                n_linhas = n_linhas + 1 #incrementa o numero de linhas contadas
        return n_linhas


def tabuleiro_celula(t,coor):
    """tabuleiro_celula: tabuleiro x coordenada -> celula
    Recebe um tabuleiro e uma coordenada e devolve a celula correspondente a essa coordenada"""
    return t[coor]

def tabuleiro_substitui_celula(t,cel,coor):
    """tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> tabuleiro
    Recebe um tabuleiro, uma celula e uma coordenada e devolve o tabuleiro que resulta da substituicao da celula existente na coordenada introduzida pela nova celula introduzida"""
    if eh_tabuleiro(t) and eh_celula(cel) and eh_coordenada(coor):  #verifica se os parametros sao validos
        t[coor] = cel
        return t
    raise ValueError ('tabuleiro_substitui_celula: argumentos invalidos')

def tabuleiro_inverte_estado(t,coor):
    """tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro
    Recebe um tabuleiro e uma coordenada e devolve o tabuleiro que resulta de inverter o estado da celula correspondente a coordenada explicitada"""
    if eh_tabuleiro(t) and eh_coordenada(coor): #verifica se os parametros sao validos
        tabuleiro_substitui_celula(t, \
                                   inverte_estado(t[coor]), coor)
        return t
    raise ValueError ('tabuleiro_inverte_estado: argumentos invalidos.')

def eh_tabuleiro(arg):
    """eh_tabuleiro: universal -> logico 
    Verifica se o argumento e do tipo tabuleiro (dicionario em que as chaves sao coordenadas e os valores associados os estados da celula da respetiva coordenada). Devolve True em caso afirmativo, False em caso contrario"""
    if not (isinstance(arg,dict) and len(arg) == 8):    #verifica se o argumento e um dicionario com 8 entradas 
        return False
    for i in arg:
        if not (eh_coordenada(i) and eh_celula(arg[i])):    
            #verifica se todas as entradas do dicionario sao coordenadas e se todos os valores sao celulas
            return False
    return True

def tabuleiros_iguais(t1,t2):
    """tabuleiros_iguais: tabuleiro x tabuleiro -> logico
    Avalia se ambos os argumentos sao tabuleiros e se sao iguais. Devolve True em caso afirmativo, False em caso contrario"""
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

def tabuleiro_para_str(t):
    """tabuleiro_str: tabuleiro -> cadeia de caracteres
    Recebe um tabuleiro (dicionario) e devolve a cadeia de caracteres que o representa (representacao externa)"""
    if eh_tabuleiro(t):
        tl = t.copy()    #tabuleiro local
        for i in tl:
            tl[i] = celula_para_str(tabuleiro_celula(tl,i))
        return ('+-------+\n|...'+tl[(0,2)]+'...|\n|..'+tl[(0,1)]+'.'\
                +tl[(1,2)]+'..|\n|.'+tl[(0,0)]+'.'+tl[(1,1)]+'.'+tl[(2,2)]\
                +'.|\n|..'+tl[(1,0)]+'.'+tl[(2,1)]+'..|\n+-------+')

def porta_x(t,p):
    """porta_z: tabuleiro x {"E", "D"} -> tabuleiro 
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_z."""     
    if not (p == 'D' or p == 'E') or not eh_tabuleiro(t):   #verifica se os parametros da funcao sao validos
        raise ValueError ('porta_x: argumentos invalidos.')
    if p == 'D':
        return tabuleiro_inverte_estado\
               (tabuleiro_inverte_estado(tabuleiro_inverte_estado(t,\
            cria_coordenada(0,1)),cria_coordenada(1,1)),cria_coordenada(2,1))
        #devolve o tabuleiro que resulta da alteracao das celulas afetadas pela porta x aplicada a direita (neste caso as celulas das coordenadas (0,1), (1,1) e (2,1))
    else:
        return tabuleiro_inverte_estado\
               (tabuleiro_inverte_estado(tabuleiro_inverte_estado(t,\
            cria_coordenada(1,0)),cria_coordenada(1,1)),cria_coordenada(1,2))
        #devolve o tabuleiro que resulta da alteracao das celulas afetadas pela porta x aplicada a esquerda (neste caso as celulas das coordenadas (1,0), (1,1) e (1,2))
    
def porta_z(t,p):
    """porta_z: tabuleiro x {"E", "D"} -> tabuleiro 
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_z."""     
    if not (p == 'D' or p == 'E') or not eh_tabuleiro(t):   #verifica se os parametros da funcao sao validos
        raise ValueError ('porta_z: argumentos invalidos.')
    if p == 'D':
        return tabuleiro_inverte_estado\
               (tabuleiro_inverte_estado(tabuleiro_inverte_estado(t,\
            cria_coordenada(0,2)),cria_coordenada(1,2)),cria_coordenada(2,2))
        #devolve o tabuleiro que resulta da alteracao das celulas afetadas pela porta z aplicada a direita (neste caso as celulas das coordenadas (0,2), (1,2) e (2,2))
    else:
        return tabuleiro_inverte_estado\
               (tabuleiro_inverte_estado(tabuleiro_inverte_estado(t,\
            cria_coordenada(0,0)),cria_coordenada(0,1)),cria_coordenada(0,2))
        #devolve o tabuleiro que resulta da alteracao das celulas afetadas pela porta z aplicada a esquerda (neste caso as celulas das coordenadas (0,0), (0,1) e (0,2))
    
    
def porta_h(t,p):
    """porta_h: tabuleiro x {"E", "D"} -> tabuleiro
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_h."""     
    if not (p == 'D' or p == 'E') or not eh_tabuleiro(t):   #verifica se os parametros da funcao sao validos
        raise ValueError ('porta_h: argumentos invalidos.')
    if p == 'D':    #quando a porta h e aplicada do lado direito, ocorre uma troca das colunas 1 e 2
        return troca_colunas(t) #as linhas e a coluna 0 mantem-se, as colunas 1 e 2 trocam
    else:   #quando a porta h e aplicada do lado esquerdo, ocorre uma troca das linhas 0 e 1
        return troca_linhas(t) #as colunas e a linha 2 mantem-se, as linhas 0 e 1 trocam
    
def troca_colunas(t):
    """troca_colunas: tabuleiro -> tabuleiro
    Recebe um tabuleiro e devolve o tabuleiro resultante da troca de todas as celulas da coluna 1 com as celulas da coluna 2"""
    for i in POSSIBILIDADES_COORDENADA:     #{0,1,2}
        celula_temporaria = tabuleiro_celula(t,cria_coordenada(i,1))    
        #celula_temporaria guarda o estado atual da celula da coluna 1, visto que o seu valor vai ser necessario posteriormente 
        tabuleiro_substitui_celula(t,tabuleiro_celula(t,\
                                cria_coordenada(i,2)),cria_coordenada(i,1))     #altera o valor da celula da coluna 1 (linha i)
        tabuleiro_substitui_celula(t,celula_temporaria,cria_coordenada(i,2))    #o valor antigo da celula da coluna 1 e aqui utilizado
    return t


def troca_linhas(t):
    """troca_linhas: tabuleiro -> tabuleiro
    Recebe um tabuleiro e devolve o tabuleiro resultante da troca de todas as celulas da linha 0 com as celulas da linha 1"""    
    for i in POSSIBILIDADES_COORDENADA:
        celula_temporaria = tabuleiro_celula(t, cria_coordenada(0,i))
        #celula_temporaria guarda o estado atual da celula da linha 0, visto que o seu valor vai ser necessario posteriormente 
        tabuleiro_substitui_celula(t,tabuleiro_celula(t,\
                                cria_coordenada(1,i)),cria_coordenada(0,i))     #altera o valor da celula da linha 0 (coluna i)
        tabuleiro_substitui_celula(t,celula_temporaria,cria_coordenada(1,i))    #o valor antigo da celula da linha 0 e aqui utilizado
    return t

def hello_quantum(s):
    """hello_quantum: cadeia de caracteres -> logico 
    Funcao principal do jogo. Recebe uma cadeia de caracteres contendo o a tabuleiro objetivo e o numero maximo de ogadas permitido. Devolve True caso o jogador tenha cumprido o objetivo e False em caso contrario"""
    conta_jogadas = 0   #contabiliza o numero de jogadas ja feitas
    tabuleiro_objetivo, max_jogadas = str_para_tabuleiro(s.split(':')[0]), \
        eval(s.split(':')[1])  #o tabuleiro_objetivo e o tabuleiro especificado no argumento ate ao caracter ":" enquanto que o numero maximo de jogadas e o valor especificado no argumento apos o caracter ":" 
    t = tabuleiro_inicial()
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:\n'\
          +tabuleiro_para_str(tabuleiro_objetivo)+\
          '\nComecando com o tabuleiro que se segue:\n'+tabuleiro_para_str(t))
    while not tabuleiros_iguais(tabuleiro_objetivo, t) \
          and conta_jogadas < max_jogadas: #enquanto o tabuleiro atual nao for igual ao tabuleiro objetivo e o jogador nao ultrapassar o numero de jogadas definido, o jogo continua
        porta = input('Escolha uma porta para aplicar (X, Z ou H): ')
        lado = input('Escolha um qubit para analisar (E ou D): ')
        if porta == 'X':
            t = porta_x(t,lado)
        elif porta == 'Z':
            t = porta_z(t,lado)
        elif porta == 'H':
            t = porta_h(t,lado)
        else:
            continue    #caso o argumento nao seja introduzido corretamente, o programa volta a pedir ao jogador para introduzir uma porta e um qubit, sem incrementar o numero de jogadas ja feitas 
        print(tabuleiro_para_str(t))
        conta_jogadas = conta_jogadas + 1
    if not tabuleiros_iguais(tabuleiro_objetivo,t): #quando o jogo termina, se os tabuleiros forem diferentes o jogador nao cumpriu o objetivo
        return False
    else: #caso os tabuleiros sejam iguais, e impressa uma mensagem de parabens que contem o numero de jogadas em que o tabuleiro foi convertido e devolve True
        print('Parabens, conseguiu converter o tabuleiro em '+\
              str(conta_jogadas)+' jogadas!')
        return True