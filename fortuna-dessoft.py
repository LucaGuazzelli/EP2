
import random

def transforma_base(listax):
    dic = {}
    for dicio in listax:
        n = dicio["nivel"]
        if n not in dic:
            dic[n] = []
        dic[n].append(dicio)
    return dic


def valida_questao(questao):
    dic = {}
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    nivels = ["facil", "medio", "dificil"]
    letras = ["A", "B", "C", "D"]
    for chave in chaves:
        if chave not in questao:
            dic[chave] = "nao_encontrado"
    if len(questao) != 4:
        dic["outro"] = "numero_chaves_invalido"
    if chaves[0] in questao:
        if questao["titulo"].strip() == "":
            dic["titulo"] = "vazio"
    if chaves[1] in questao:
        if questao["nivel"] not in nivels:
            dic["nivel"] = 'valor_errado'
    if chaves[2] in questao:
        if len(questao["opcoes"]) != 4:
            dic["opcoes"] = 'tamanho_invalido'
        else:
            for option in letras:
                if option not in questao["opcoes"]:
                    dic["opcoes"] = "chave_invalida_ou_nao_encontrada"
            for option in letras:
                if questao["opcoes"][option].strip() == "":
                    if "opcoes" not in dic: 
                        dic["opcoes"] = {f'{option}': 'vazia'}
                    else:
                        dic["opcoes"][option]  = "vazia"
    if chaves[3] in questao:
        if questao["correta"] not in letras: 
            dic["correta"] = 'valor_errado'
    return dic 
        

def valida_questoes(lista):
    prob_identificados = []
    for questao in lista:
        prob_identificado = valida_questao(questao)
        prob_identificados.append(prob_identificado)
    return prob_identificados
 

def sorteia_questao (dicio, nivel):
    max = len(dicio[nivel])
    num = random.randint(0,max-1)
    perg_sor = dicio[nivel][num]
    return perg_sor 


def sorteia_questao_inedita (dicio, nivel, lista):
    max = len(dicio[nivel])
    num = random.randint(0,max-1)
    perg_sor = dicio[nivel][num]
    while perg_sor in lista:
        num = random.randint(0,max-1)
        perg_sor = dicio[nivel][num]
    lista.append(perg_sor)
    return perg_sor
    

def questao_para_texto(questao, id):
    return f"------------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\nA: {questao['opcoes']['A']}\nB: {questao['opcoes']['B']}\nC: {questao['opcoes']['C']}\nD: {questao['opcoes']['D']}"
    

def gera_ajuda(questao):
    lista = [ "A", "B", "C", "D"]
    lista.remove(questao["correta"])
    n = 1
    dica = []
    max = 3
    qtsorteio = random.randint(1,2)
    sor_per = random.randint(1,max-1)
    while qtsorteio >= n:
        sor_per = random.randint(0,max-1)
        if questao["opcoes"][lista[sor_per]] not in dica:
            dica.append(questao["opcoes"][lista[sor_per]])
            n = n + 1
    dicas = " | ".join(dica)
    return f"DICA:\nOpções certamente erradas: {dicas}"



    

    