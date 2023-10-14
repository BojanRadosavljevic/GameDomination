tabela = []
moves = 0
firstPlayer = 0
covek = [0,0]
racunar = [0,0]
m = 0
n = 0
listaMogucihPoteza=[]
nextMove=[]
lokalNextMove=[]
brojacDubine=3
brojacPoteza=0

def unosParametaraIgre():
    global m, n
    m = int(input("Unesite broj vrsta table(n): "))
    n = int(input("Unesite broj kolona table(m): "))

def kreiranjeTabele():
    for i in range(0, m):
        pom = []
        for j in range(0, n):
            pom.append(' ')
        tabela.append(pom)

def prikazTabele() -> list[object]:
    tabelaZaPrikaz = []
    for i in range(0, m):
        listaZaDodavanje = []
        if i == 0:
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append(chr(65 + j))
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append('=')
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(str(i + 1))
            listaZaDodavanje.append('||')
            for j in range(0, n):
                listaZaDodavanje.append(tabela[i][j])
                listaZaDodavanje.append('|')
            listaZaDodavanje.append('|')
            listaZaDodavanje.append(str(i + 1))
            tabelaZaPrikaz.append(listaZaDodavanje)
        elif i == m-1:
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append('-')
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(str(i + 1))
            listaZaDodavanje.append('||')
            for j in range(0, n):
                listaZaDodavanje.append(tabela[i][j])
                listaZaDodavanje.append('|')
            listaZaDodavanje.append('|')
            listaZaDodavanje.append(str(i + 1))
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append('=')
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append(chr(65 + j))
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
        else:
            listaZaDodavanje = []
            listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            for j in range(0, n):
                listaZaDodavanje.append('-')
                listaZaDodavanje.append(' ')
            listaZaDodavanje.append(' ')
            tabelaZaPrikaz.append(listaZaDodavanje)
            listaZaDodavanje = []
            listaZaDodavanje.append(str(i + 1))
            listaZaDodavanje.append('||')
            for j in range(0, n):
                listaZaDodavanje.append(tabela[i][j])
                listaZaDodavanje.append('|')
            listaZaDodavanje.append('|')
            listaZaDodavanje.append(str(i + 1))
            tabelaZaPrikaz.append(listaZaDodavanje)
    for i in tabelaZaPrikaz:
        for j in i:
            print(j, end='')
        print('\n')  

def firstPlayer():
    global firstPlayer, human, computer,nextMove,lokalNextMove,covek,racunar
    prvi = int(input("Odaberite ko bira prvi, 1. covek ili 2. racunar(unesite 1 ili 2): "))
    if(prvi != 1 and prvi != 2):
        firstPlayer()
    if(prvi == 1):
        human = True
        computer=False
        covek[0] = 1
        racunar[0] = 2
        covek[1] = "X"
        racunar[1] = "O"
    else:
        computer = True
        human=False
        covek[0] = 2
        racunar[0] = 1
        covek[1] = "O"
        racunar[1] = "X"
    firstPlayer = prvi
    if human==True:
        nextMove=covek
        lokalNextMove=covek
    else:
        nextMove=racunar
        lokalNextMove=racunar

def unosVrste():
    vr = (input("Unesite vrstu poteza (broj od 1 do "+str(m)+ "): "))
    return vr
    
def unosKolone():
    kol = input("Unesite kolonu poteza (karakter od A do "+chr(ord("A")+n-1)+"): ") 
    return kol

def move():
    global tabela,n,m,nextMove,covek,racunar,lokalNextMove,brojacDubine,brojacPoteza
    vr = False
    kol = False
    potez = [0,0]
    #ovde se poziva minimax
    if human:
        vrsta = unosVrste()
        kolona = unosKolone()
        nextMove=racunar
        lokalNextMove=racunar
        while (not vr):
            if ord(vrsta)<ord("1") or ord(vrsta)>ord("9"):
                vrsta = unosVrste()
            else:
                vrsta=int(vrsta)-1
                if (vrsta >= 0 and vrsta < m):
                    potez[0] = vrsta
                    vr = True
                else:
                    vrsta = unosVrste()
        while (not kol):
            if (ord(kolona) >= ord("A")  and  ord(kolona) <= ord("A")+n):
                potez[1] = kolona
                kol = True
            else:
                kolona = unosKolone()
    else:
        if human==True:
            potezSl=minimax(tabela,brojacDubine,human)
        else:
            potezSl=minimax(tabela,brojacDubine,human)      
        if brojacPoteza==(n+m)/3-1:
            brojacDubine=brojacDubine+1
        else:
            brojacPoteza=brojacPoteza+1
        nextMove=covek
        lokalNextMove=covek
        vrsta=potezSl[0][1][0]
        kolona=potezSl[0][1][1]
        potez[0]=vrsta
        potez[1]=kolona
    if (len(potez) != 2):
        move()
    validMove(potez)

def whoMoves():
    global human, computer, firstPlayer,listaMogucihPoteza
    if (firstPlayer == 1):
        human = False
        computer = True
        firstPlayer = 2
    else:
        human = True
        computer = False
        firstPlayer = 1

def validMove(mv):
    global moveIsValid, human, listaMogucihPoteza
    moveIsValid = False
    if (human):
        if(covek[1] == "X"):
            isValidX(mv)
        else:
            isValidO(mv)
    else:
        if(racunar[1] == "X"):
            isValidX(mv)
        else:
            isValidO(mv)
    if(moveIsValid):
        moveIsValid = False
        prikazTabele()
        whoMoves()
        listaMogucihPoteza=[]
        if not human:
            listaMogucihPoteza=proveriMogucePoteze(tabela,nextMove[1])
            print(listaMogucihPoteza)
        else:
            listaMogucihPoteza=proveriMogucePoteze(tabela,nextMove[1])
            print(listaMogucihPoteza)
        if listaMogucihPoteza==[]:
            if human:
                print("kraj igre racunar je pobedio")
            else:
                print("kraj igre igrac je pobedio")
            return
        listaMogucihPoteza=[]
        move()


def isValidX(mv):
    global moveIsValid
    ch = ord(mv[1]) - ord("A")
    if (mv[0] < 1):
        print("Nevalidan potez!")
        move()
    elif (tabela[int(mv[0])][ch] != ' '  or  tabela[int(mv[0])-1][ch] != ' '):
        print("Polje na tabeli je vec zauzeto!")
        move()
    else:
        print("isValidX")
        moveIsValid = True
        tabela[int(mv[0])][ch] = "X"
        tabela[int(mv[0])-1][ch] = "X"



def isValidO(mv):
    global moveIsValid
    print(moveIsValid)
    ch = ord(mv[1]) - ord("A")
    if (ord(mv[1]) - ord("A") > n-2):
        print("Nevalidan potez!")
        move()
    elif (tabela[int(mv[0])][ch] != ' '  or  tabela[int(mv[0])][ch+1] != ' '):
        print("Polje je vec zauzeto!")
        move()
    else:
        moveIsValid = True
        tabela[int(mv[0])][ch] = "O"
        tabela[int(mv[0])][ch+1] = "O"


def proveriMogucePoteze(tabla,mv)->list[list]:
    global listaMogucihPoteza
    mpot=[]
    for i in range(0,m):
        for j in range(0,n):
            if mv=="X":
                if i!=0 :
                    if tabla[i][j]==' ' and tabla[i-1][j]==' ':
                        mpot.append(i)
                        mpot.append(chr(j+ord('A')))
                        listaMogucihPoteza.append((None,mpot))
                        mpot=[]
            elif mv=="O":
                if j!=n-1 :
                    if tabla[i][j]==' ' and tabla[i][j+1]==' ':
                        mpot.append(i)
                        mpot.append(chr(j+ord('A')))
                        listaMogucihPoteza.append((None,mpot))
                        mpot=[]
    return listaMogucihPoteza
# 3 faza dodato
def movemm(potez,mv,tabla):
        global lokalNextMove
        if mv == "X":
            ch = ord(potez[1][1]) - ord("A")
            tabla[int(potez[1][0])][ch] = "X"
            tabla[int(potez[1][0])-1][ch] = "X"
            lokalNextMove=racunar
        else:
            ch = ord(potez[1][1]) - ord("A")
            tabla[int(potez[1][0])][ch] = "O"
            tabla[int(potez[1][0])][ch+1] = "O"
            lokalNextMove=covek
        return tabla

def minimax(tabela,dubina,human,alfa=(None,-100),beta=(None,100)):
    tabla=[]
    mini=[]
    for i in range(0,m):
        mini=tabela[i].copy()
        tabla.append(mini)
    if racunar[1]=="X":
        return maxValue(tabla,dubina,alfa,beta)
    else:
        return minValue(tabla,dubina,alfa,beta)

def maxValue(tabla,dubina,alfa,beta,potez=None):
    global listaMogucihPoteza,lokalNextMove,covek
    listaMogucihPoteza=[]
    listaPoteza=list(proveriMogucePoteze(tabla,"X"))
    if dubina==0 or listaPoteza is None or len(listaPoteza)==0:
        return (potez,evaluate(potez,tabla))
    else:
        for st in listaPoteza:
            lokTabla=[]
            mini=[]
            for i in range(0,m):
                mini=tabla[i].copy()
                lokTabla.append(mini)
            alfa=max(alfa,minValue(movemm(st,"X",lokTabla),dubina-1,alfa,beta,st if potez is None else potez),key=lambda x:x[1])
        if alfa[1]>beta[1]:
            return beta
    return alfa

def minValue(tabla,dubina,alfa,beta,potez=None):
    global listaMogucihPoteza,lokalNextMove,racunar
    listaMogucihPoteza=[]
    listaPoteza=list(proveriMogucePoteze(tabla,"O"))
    if dubina==0 or listaPoteza is None or len(listaPoteza)==0:
        return (potez,evaluate(potez,tabla))
    else:
        for st in listaPoteza:
            lokTabla=[]
            mini=[]
            for i in range(0,m):
                mini=tabla[i].copy()
                lokTabla.append(mini)
            beta=min(beta,maxValue(movemm(st,"O",lokTabla),dubina-1,alfa,beta,st if potez is None else potez),key=lambda x:x[1])
        if beta[1]<=alfa[1]:
            return alfa
    return beta

def evaluate(mv,tabla)->int:
    listaMogucihPotezaX=0
    listaMogucihPotezaO=0
    brojSafePotezaX=0
    brojSafePotezaO=0
    for i in range(0,m):
        for j in range(0,n):
                if i!=0 :
                    if tabla[i][j]==' ' and tabla[i-1][j]==' ':
                        listaMogucihPotezaX=listaMogucihPotezaX+1
                        if j==0:
                            if tabla[i][j+1]!=' ' and tabla[i-1][j+1]!=' ':
                                brojSafePotezaX=brojSafePotezaX+1
                        if j==n-1:
                            if tabla[i][j-1]!=' ' and tabla[i-1][j-1]!=' ':
                                brojSafePotezaX=brojSafePotezaX+1
                        else:
                            if tabla[i][j-1]!=' ' and tabla[i-1][j-1]!=' ' and tabla[i][j+1]!=' ' and tabla[i-1][j+1]!=' ':
                                brojSafePotezaX=brojSafePotezaX+1
                if j!=n-1 :
                    if tabla[i][j]==' ' and tabla[i][j+1]==' ':
                        listaMogucihPotezaO=listaMogucihPotezaO+1
                        if i==0:
                            if tabla[i+1][j]==' ' and tabla[i+1][j+1]==' ':
                                brojSafePotezaO=brojSafePotezaO+1
                        if i==n-1:
                            if tabla[i-1][j]==' ' and tabla[i-1][j+1]==' ':
                                brojSafePotezaO=brojSafePotezaO+1
                        else:
                            if tabla[i+1][j]==' ' and tabla[i+1][j+1]==' ' and tabla[i-1][j]==' ' and tabla[i-1][j+1]==' ':
                                brojSafePotezaO=brojSafePotezaO+1
    vrednost=listaMogucihPotezaX-listaMogucihPotezaO+brojSafePotezaX-brojSafePotezaO    
    return vrednost

unosParametaraIgre()
kreiranjeTabele()
prikazTabele()
firstPlayer()
move()