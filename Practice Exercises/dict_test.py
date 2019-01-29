# Organizing people's data using dictionaries in a list
def consolidar(inf):
    cons = []
    dic = {}
    j = 0
    loop = True
    while loop:
        for k in inf.keys():
            # In other words, if j is less than/equal to the length of the
            # lists in the dictionary.
            try:
                dic[k]=inf[k][j]
            except:
                loop = False
        if len(dic)>0: cons.append(dic)
        if loop: j = j + 1
        dic = {}
    return cons

info = {'nombres':['esteban', 'ferney', 'gisela','wilfredo','juan'],
'apellidos':['quevedo','forero','gomez','moreno','torres'],
'ciudades':['bogota','popayan','san gil','merida','bucaramanga']}
consolidado = consolidar(info)
print(consolidado)
