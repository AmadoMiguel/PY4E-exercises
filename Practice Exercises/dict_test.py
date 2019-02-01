# Organizing people's data using dictionaries in a list.
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
# Second way to achieve this.
def consolidarSecondWay(inf):
    for k in inf.keys():
        # Determine the length of the lists (assuming all the lists in info are
        # the same size).
        l = len(inf[k])
        break
    cons = [ {k:inf[k][j] for k in info.keys()} for j in range(0,l) ]
    return cons

# DIctionary containing some information.
info = {'name':['esteban', 'ferney', 'gisela','wilfredo','juan'],
'last_name':['quevedo','forero','gomez','moreno','torres'],
'city':['bogota','popayan','san gil','merida','bucaramanga']}

consolidado = consolidar(info)
consolidado_secondWay = consolidarSecondWay(info)
print(consolidado)
print('\n',consolidado_secondWay)
