import re

def le_assinatura():

    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    somatorio = 0
    for i in range(6):
        somatorio += abs(as_a[i]-as_b[i])
    
    Sab = somatorio/6                    
    
    return Sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    lista = []
    numCaracteres, numPalavras, numFrases, numSentencas, numCaracteresSentencas, numCaracteresFrases, numPalavrasDiferentes,numPalavrasUnicas = 0, 0, 0, 0, 0, 0, 0, 0
    sentencas = separa_sentencas(texto)
    numSentencas += len(sentencas)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        numCaracteresSentencas += len(sentenca)
        numFrases += len(frases)
        for frase in frases:
            palavras = separa_palavras(frase)
            numCaracteresFrases += len(frase)
            numPalavras += len(palavras)            
            for i in range(len(palavras)):
                numCaracteres += len(palavras[i])
                lista.append(palavras[i])
    numPalavrasDiferentes = n_palavras_diferentes(lista)
    numPalavrasUnicas = n_palavras_unicas(lista)
    mediaPalavra = numCaracteres / numPalavras
    relacaoTypeToken = numPalavrasDiferentes / numPalavras
    razaoHapaxLegomana = numPalavrasUnicas/ numPalavras
    mediaSentenca = numCaracteresSentencas / numSentencas
    complexidadeSentenca = numFrases / numSentencas
    mediaFrase = numCaracteresFrases / numFrases
    resposta = []
    resposta.append(mediaPalavra)
    resposta.append(relacaoTypeToken)
    resposta.append(razaoHapaxLegomana)
    resposta.append(mediaSentenca)
    resposta.append(complexidadeSentenca)
    resposta.append(mediaFrase)
    return resposta

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    compara = []
    for texto in textos:
        assTexto = calcula_assinatura(texto)
        compara.append (compara_assinatura(assTexto, ass_cp))
    cohpiah = compara [0]
    i = 1
    for i in range(1, len(compara)):
        if compara[i] <= cohpiah:
            cohpiah = i+1
    
    return cohpiah

assinatura = le_assinatura()
textos = le_textos()
cohpiah = avalia_textos(textos, assinatura) 
print("O autor do texto",(cohpiah),"está infectado com COH-PIAH")
    
