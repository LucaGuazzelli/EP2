def transforma_base(listax):
    dic = {}
    for dicio in listax:
        n = dicio["nivel"]
        if n not in dic:
            dic[n] = []
        dic[n].append(dicio)
    return dic