#pip install numpy
#pip install scipy
#pip install sklearn
#pip install graphviz
#N�o lembro se tem mais alguma, mas ele avisa quando vai rodar
from sklearn import tree
from randomList1 import randomList
from graphviz import *
import graphviz

#FUN��O QUE SEPARA AS POTENCIAS DAS �REAS, DEIXANDO AS 2 EM LISTAS DIFERENTES
#valores: S�o as potencias, classes: s�o as �reas
#Lembrando q ela se baseia em como as listas da randomList v�o ser retornadas
def criarDataList(lista):
    valores = []
    classes = []
    for i in range(len(lista)):
        nlista = lista[i].split(";")
        temp = [float(nlista[0]), float(nlista[1]), float(nlista[2])]
        temp2 = [nlista[3]]
        valores.append(temp)
        classes.append(temp2)
    return valores, classes

#nome: Arquivo com as informa��es de todas as �rvores
#� por ele que da pra saber qual �rvore � a melhor
#Basta usar o comando CTRL + F e procurar por "Acertos:"
#Depois dos ":" nem "Acertos:" vc digita a quantidade acertos ue quer procurar, m�ximo � 32
#Por que s�o 65 linhas de informa��es em mediana
nome = "Dados das Arvores.txt"
dados = open(nome, "w")

#Esse range � o n�mero de �rvores
#Por exemplo se 100000, v�o ser 100000 arvoresmed = arvores de media
#E sem 100000 arvoresmdn = arvores de mediana
for i in range(100000):
    #Os arquivos precisam estar na msm pasta, favor n�o esquecer
    #med: Padr�o para qualquer coisa q envolva dados por m�dia
    #mdn: Padr�o para qualquer coisa q envolva dados por mediana
    arq_med = open("base-media-cultura.csv","r")
    arq_mdn = open("base-mediana-cultura.csv","r")

    #Tirando a 1 posi��o dos docs, j� que ela � s� informa��o sobre as colunas, que � essa na linha de baixo no caso
    #publi0;publi1;publi2;area
    instancias_med = arq_med.read().split("\n")
    instancias_med = instancias_med[1:]
    instancias_mdn = arq_mdn.read().split("\n")
    instancias_mdn = instancias_mdn[1:]

    #n�o precisa do aux_med e do aux_mdn, euu s� tava testando coisa e esqueci de tirar
    aux_med = instancias_med
    aux_mdn = instancias_mdn

    #tt_med = Lista com os testes para a m�dia
    #to_med = Lista com os treinamentos para a m�dia
    #tt_mdn = Lista com os testes para a mediana
    #to_mdn = Lista com os treianmentos para a mediana
    tt_med, to_med = randomList(aux_med)
    tt_mdn, to_mdn = randomList(aux_mdn)
    #treino_med = Lista com as potencias para o treinamento da m�dia
    #y_to = Lista com as �reas para o treinamento da m�dia
    #teste_med = Lista com as potencias para o teste da m�dia
    #y_tt = Lista com as �reas para o teste da m�dia
    treino_med, y_to  = criarDataList(to_med)
    teste_med, y_tt = criarDataList(tt_med)
    treino_mdn, z_to = criarDataList(to_mdn)
    teste_mdn, z_tt = criarDataList(tt_mdn)

    #gini = � meio q o grau de inclina��o da �rvore se eu entendi certo
    #Os outro eu n sei explicar bem
    #clf = �rvore para media
    #clf1 = �rvore para mediana
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    clf = clf.fit(treino_med, y_to)

    clf1 = tree.DecisionTreeClassifier(criterion = "entropy")
    clf1 = clf1.fit(treino_mdn, z_to)

    #Vou simplicar
    #acertos_med_R = quantas classes ela acertou de vdd
    #erros_med_r = quantas classes ela errou
    #acertos_med_P =  quantas classes ela devia ter acertado, pode chamar de total
    #Mesma coisa para os mdn = mediana
    #valor[0] = � a classe que ele preveu, no nosso caso a �rea
    num_arv = str(i)
    nome_arv = "Arvore" + num_arv
    arv_med = nome_arv + "media.txt"
    arv_mdn = nome_arv + "mediana.txt"
    dados_med = open(arv_med, "w")
    dados_mdn = open(arv_mdn, "w")
    acertos_med_P = len(teste_med)
    acertos_med_R = 0
    erros_med_R = 0
    classes_med = []
    classes_mdn = []
    for k in range(len(teste_med)):
        valor = clf.predict([teste_med[k]])
        dados_med.writelines(str(teste_med[k][0]) + ";" + str(teste_med[k][1]) + ";" + str(teste_med[k][2]) + ";" + valor[0] + "\n")
        classes_med.append(valor[0])
        if valor[0] == y_tt[k][0]:
            acertos_med_R += 1
        else:
            erros_med_R += 1        

    acertos_mdn_P = len(teste_med)
    acertos_mdn_R = 0
    erros_mdn_R = 0
    for p in range(len(teste_mdn)):
        valor = clf1.predict([teste_mdn[p]])
        dados_mdn.writelines(str(teste_mdn[k][0]) + ";" + str(teste_mdn[k][1]) + ";" + str(teste_mdn[k][2]) + ";" + valor[0] + "\n")
        classes_mdn.append(valor[0])
        if valor[0] == z_tt[k][0]:
            acertos_mdn_R += 1
        else:
            erros_mdn_R += 1
    dados_med.close()
    dados_mdn.close()
    #Escrever Dados em txt
    texto_med = "Acertos:" + str(acertos_med_R) + ";" + "Erros:" + str(erros_med_R) + ";" + "Total:" + str(acertos_med_P)
    texto_mdn = "Acertos:" + str(acertos_mdn_R) + ";" + "Erros:" + str(erros_mdn_R) + ";" + "Total:" + str(acertos_mdn_P)
    dados.writelines(nome_arv + "\n")
    dados.writelines("M�dia" + "\n")
    dados.writelines(texto_med + "\n")
    dados.writelines("Mediana" + "\n")
    dados.writelines(texto_mdn + "\n")
    dados.writelines("---------" + "\n")
    namemed = "arvoremed" + num_arv
    namemdn = "arvoremdn" + num_arv
    #Para saber em que posicao do range gigantesco ele t�
    print(i)
    #As duas arvores sendo esportadas para arquivos
    #S� abrir no sublime, que vai da pra ver o que tem nele
    dot_med = tree.export_graphviz(clf, out_file=namemed)
    dot_mdn = tree.export_graphviz(clf1, out_file=namemdn)
dados.close()
