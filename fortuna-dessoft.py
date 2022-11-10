class ANSI():   
    def color_text(code): 
        return "\33[{code}m".format(code=code)


import random

lista_premiacao = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]

premiacao = 0

quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

lista = [] 

def transforma_base(quest):
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
 

def sorteia_questao (perguntas, nivel):
    max = len(dicio[nivel])
    num = random.randint(0,max-1)
    perg_sor = dicio[nivel][num]
    return perg_sor 


def sorteia_questao_inedita (perguntas, nivel, lista):
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


print((ANSI.color_text(95)) + "Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n")

nome = input(ANSI.color_text(39) + "Qual seu nome?")

print(f'\n\n ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n\n')

print(input("Aperte ENTER para continuar..."))

print(ANSI.color_text(39) + '\n\n O jogo já vai começar! Lá vem a primeira questão!') + '\n' + '\n' + (ANSI.color_text(39) + 'Vamos começar com questões do nível FACIL!') + '\n' + (ANSI.color_text(39) + "Aperte ENTER para continuar...")

qt_ajuda = 0 
qt_pula = 0 
qt_parar = 0 
premiacao = 0
qt_certo = 0  
count_facil = 0 
count_medio = 0
count_dificil = 0  


while resposta != "parar":

    perguntas = transforma_base(quest)

    nivel = "FACIL"

    count_facil = count_facil + 1

    if len(perguntas["facil"]) > count_facil:
        nivel = "medio"
        count_medio = count_medio + 1
        if len(perguntas["medio"]) > count_medio:
            nivel = "dificil"
            count_dificil = count_dificil + 1
            if len(perguntas["dificil"]) > count_dificil:
                resposta = "parar"


    perguntas_sorteadas = sorteia_questao_inedita (perguntas, nivel, lista)

    pergunta_apresentada = questao_para_texto(perguntas_sorteadas, id)

    resposta = input("Qual sua resposta?! ")

    if resposta == quest[id]["correta"]:
        premiacao = premiacao + lista_premiacao[qt_certo]
        qt_certo = qt_certo + 1
        print(f"Você acertou! Seu prêmio atual é de R$ {premiacao:2f}")
        print(input(ANSI.color_text(39) + "Aperte ENTER para continuar..."))
        else:
            print("Que pena! Você errou e vai sair sem nada :(")
            premiacao = 0 

    if resposta == "pular":
        qt_pula = qt_pula + 1

        if qt_pula > 3:
    if resposta == "ajuda":
        dica = gera_ajuda(pergunta_apresentada)



    
