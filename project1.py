#92560, Susana Monteiro

def eh_tabuleiro(tab):
    """eh_tabuleiro: universal -> booleano 
    Recebe um tuplo e devolve True se este corresponder a tabuleiro valido, False caso contrario."""
    possibilidades = (0,1,-1)   #todos os elementos do tabuleiro tem de ser 0, 1 ou -1
    if not (isinstance(tab,tuple) and len(tab) == 3): #verifica se o argumento e um tuplo com 3 elementos
        return False
    for i in range(len(tab)):
        if not isinstance(tab[i],tuple):    #verifica se todos os elementos do tuplo sao tuplos
            return False
        if not ((i == 2 and len(tab[i]) == 2) or ((i == 0 or i == 1) and len(tab[i]) == 3)):  #verifica as dimensoes dos tuplos que constituem o tabuleiro
            return False
        for l in tab[i]:
            if l not in possibilidades: #verifica se todos os elementos do tuplo sao 0, 1 ou -1
                return False
    return True

def tabuleiro_str(tab):
    """tabuleiro_str: tabuleiro -> cadeia de caracteres
    Recebe um tuplo e devolve a cadeia de caracteres que o representa."""
    if not eh_tabuleiro(tab): #avalia se o tuplo de entrada e um tabuleiro valido
        raise ValueError ("tabuleiro_str: argumento invalido")
    novo_t = () #tuplo que vai guardar o resultado da troca de todos os elementos -1 do tabuleiro por x
    for t in tab:
        for i in range(len(t)):
            if t[i] == -1: 
                t = t[:i] + ('x',) + t[i+1:] #substitui por x cada elemento igual a -1 de cada subtuplo 
        novo_t = novo_t + t #junta ao novo_t o subtuplo que contem x no lugar de -1
    return ("+-------+\n|...{t[2]}...|\n|..{t[1]}.{t[5]}..|\n|.{t[0]}.{t[4]}.{t[7]}.|\n|..{t[3]}.{t[6]}..|\n+-------+".format(t = novo_t))        
    
def tabuleiros_iguais(tab1,tab2):
    """tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    Recebe dois tabuleiros e devolve True se os tabuleiros sao iguais e False caso contrario."""
    if not (eh_tabuleiro(tab1) and eh_tabuleiro(tab2)): #verificar se ambos os tuplos sao tabuleiros validos
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")
    for t in range(len(tab1)):  #comparar os elementos dos dois tuplos um a um
        for i in range(len(tab1[t])):
            if tab1[t][i] != tab2[t][i]:
                return False    #assim que for encontrado um par de elementos diferentes, a funcao devolve False
    return True #em caso contrario, se todos os elementos forem iguais, a funcao devolve True

def calcula(c1,c2): 
    """calcula: inteiro x inteiro -> inteiro
    Calcula o novo valor de uma celula, de acordo com o valor das duas celulas de que depende, e devolve o novo valor."""
    if c1 == -1 or c2 == -1:    #no caso de uma das celulas do qubit ser -1 (estado incerto), aquela que se pretende calcular sera necessariamente -1
        return -1
    return (c1+c2) % 2 #se as celulas tiverem o mesmo valor, entao a celula calculada tera o valor de 0 (preta - inativa); em caso contrario, tera o valor de 1 (branca - ativa)

def porta_x(tab,e_d):
    """porta_x: tabuleiro x {"E", "D"} -> tabuleiro
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_x.""" 
    if not (e_d == 'D' or e_d == 'E') or not eh_tabuleiro(tab): #verifica se os parametros da funcao sao validos
        raise ValueError ("porta_x: um dos argumentos e invalido")
    elif e_d == 'D':
        if tab[2][0] == -1: #se o valor for -1, a celula permanece com o valor de -1
            return tab
        alt = abs(tab[2][0]-1) #altera o valor da celula a que foi aplicada a porta x
        return (tab[0][0],calcula(tab[0][0],alt),tab[0][2]),(tab[1][0],calcula(tab[1][0],alt),tab[1][2]),(alt, tab[2][1]) #constroi o novo tuplo, consequente da alteracao resultante da aplicacao da porta x a celula 
    else:
        if tab[1][0] == -1:
            return tab
        alt = abs(tab[1][0]-1)
        return tab[0],(alt,calcula(alt,tab[2][0]),calcula(alt,tab[2][1])),tab[2]
    
def porta_z(tab,e_d):
    """porta_z: tabuleiro x {"E", "D"} -> tabuleiro 
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_z.""" 
    if not (e_d == 'D' or e_d == 'E') or not eh_tabuleiro(tab): #verifica se os parametros da funcao sao validos
        raise ValueError ("porta_z: um dos argumentos e invalido")
    elif e_d == 'D':
        if tab[2][1] == -1: #se o valor for -1, a celula permanece com o valor de -1
            return tab
        alt = abs(tab[2][1]-1) #altera o valor da celula a que foi aplicada a porta z
        return (tab[0][0],tab[0][1],calcula(tab[0][0],alt)),(tab[1][0],tab[1][1],calcula(tab[1][0],alt)),(tab[2][0], alt) #constroi o novo tuplo, consequente da alteracao resultante da aplicacao da porta z a celula
    else:
        if tab[0][0] == -1:
            return tab
        alt = abs(tab[0][0]-1)
        return (alt,calcula(alt,tab[2][0]),calcula(alt,tab[2][1])),tab[1],tab[2] 
    
def porta_h(tab,e_d):
    """porta_h: tabuleiro x {"E", "D"} -> tabuleiro
    Recebe um tabuleiro e um caracter ("E" ou "D") e devolve um novo tabuleiro consequente da aplicacao da funcao porta_h.""" 
    if not (e_d == 'D' or e_d == 'E') or not eh_tabuleiro(tab): #verifica se os parametros da funcao sao validos
        raise ValueError ("porta_h: um dos argumentos e invalido")
    elif e_d == 'D':
        nt = tab[0],tab[1],(tab[2][1],tab[2][0]) #nt = novo tabuleiro - as celulas do qubit afetado pela porta h trocam de estado entre si
    else:
        nt = ((tab[1][0],) + tab[0][1:],(tab[0][0],) + tab[1][1:],tab[2])
    return (nt[0][0],calcula(nt[0][0],nt[2][0]),calcula(nt[0][0],nt[2][1])),(nt[1][0],calcula(nt[1][0],nt[2][0]),calcula(nt[1][0],nt[2][1])),(nt[2][0],nt[2][1]) 
    #constroi o novo do tuplo, conforme as alteracoes aplicadas pela porta h nas celulas
