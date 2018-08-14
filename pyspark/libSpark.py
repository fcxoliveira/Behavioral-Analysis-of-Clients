# ARVORE QUE DETERMINA QUAL AREA O MAC ESTAVA
class ArvoreDecideCaminho():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def predicao(self):
        classe = ""
        #self.x = publish 0 - node 0 
        #self.y = publish 0 - node 1
        #self.z = publish 0 - node 2
        if(self.x <= -79.0):

            if(self.y <= -81.9):

                if(self.z <= -79.835):

                    if(self.x <= -93.5):

                        if(self.y <= -94.5):
                            classe = "fora"

                        else:
                            if(self.y <= -86.0):
                                classe = "banca-infantil"
                            else:
                                classe = "fora"

                    else:
                        if(self.x <= -86.165):
                            classe = "banca-infantil"
                        else:
                            classe = "entrada"
                else:
                    classe = "geek"

            else:

                if(self.y <= -78.675):

                    if(self.x <= -86.25):
                        classe = "geek"
                    else:
                        classe = "artes"
                else:
                    if(self.z <= -76.335):

                        if(self.y <= -76.72):

                            if(self.z <= -90.25):
                                classe = "fora"
                            else:
                                classe = "entrada"
                        else:
                            classe = "caixa"
                    else:
                        classe = "geek"

        else:

            if(self.x <= -61.125):

                if(self.y <= -78.57):
                    if(self.y <= -91.0):
                        classe = "cd"
                    else:
                        classe = "banca-infantil"
                else:
                    if(self.z <= -95.5):
                        classe = "leitura2"
                    else:
                        classe = "artes"
            else:
                if(self.y <= -79.375):
                    classe = "leitura1"

                else:
                    if(self.y <= -50.68):
                        classe = "leitura1"
                    else:
                        classe = "leitura1"
        return classe

#FUNCAO QUE CALCULA A MEDIA DAS POTENCIAS
def getCalc(lista):
    calc =  0
    cont = 0
    potencia = 0
    if(type(lista).__name__ == "list"):
        for i in range(len(lista)):
            potencia = float(lista[i])
            if(potencia == 0.0):
                pass
            else:
                calc += potencia
                cont += 1
    else:
        cont += 1
        potencia = float(lista)
        calc = potencia
    if(potencia != 0 and cont != 0):
        calc = calc/cont
    else:
        calc = -100.00
    result = calc
    return result
def getResultTree(lista):
    print(lista)
    mac = lista[0]
    infos = lista[1]
    x = float(infos[0])
    y = float(infos[1])
    z = float(infos[2])
    arv = ArvoreDecideCaminho(x, y, z)
    area = arv.predicao()
    result = (mac, area)
    return result
    
#FUNCAO PARA RETORNAR O MAC COMO CHAVE E AS POTENCIAS COMO VALOR
def getLine(line):
    mac = line.split(" ")[1]
    p1 = line.split(" ")[3]
    p2 = line.split(" ")[4]
    p3 = line.split(" ")[5]
    return (mac, [p1, p2, p3])

#FUNCAO QUE COLOCA AS POTENCIAS DO MESMO PUBLISH EM LISTAS IGUAIS
def getAppend(a, b):
    p = [[],[],[]]
    if(a == None):
        pass
    elif(b == None):
        pass
    elif(a != None and b != None):
        for i in range(3):
            if(type(a[i]).__name__ == "list"):
                p[i].extend(a[i])
            else:
                p[i].append(float(a[i]))
            if(type(b[i]).__name__ == "list"):
                p[i].extend(b[i])
            else:
                p[i].append(float(b[i]))
    return p

#ORGANIZA AS LISTAS PARA A ENTRADA DA ARVORE
def getOrganize(linha):
    # lista = [(mac, [])]
    mac = linha[0]
    allP = linha[1]
    p1 = 0.00
    p2 = 0.00
    p3 = 0.00
    for i in range(3):
        p1 = getCalc(allP[0])
        p2 = getCalc(allP[1])
        p3 = getCalc(allP[2])
    newLinha = (mac, [p1, p2, p3])
    return newLinha