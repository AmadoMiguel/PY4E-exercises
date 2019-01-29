# First repeated number in a list of numbers
def primerDuplic(numList):
    # Create a copy of the original list and invert it
    invList = numList
    invList.reverse()
    # Prepare the histogram
    dic = {}
    primRep = None
    for num in numList:
        # numList histogram
        dic[num] = dic.get(num,0) + 1
    # Check for repeated numbers
    for num,rep in dic.items():
        # If a number appears more than once in numList
        if rep > 1:
            # Ask for the index in the inverted list, so it actually finds the
            # first repeated number index, not the last.
            ind = invList.index(num)
            # Determine the index of the first repeated number
            if primRep == None or primRep<ind:
                primRep = ind
    if primRep == None:
        return None
    else:
        # Returns the index of the first repeated number
        return primRep
lista = [1,2,9,0,7,3,9,3,4,6]
primerDup = primerDuplic(lista)
if primerDup == None:
    print("There aren't repeated numbers")
else:
    print('First repeated number:',lista[primerDup])

# Organizing people's data using dictionaries in a list
def consolidar(l1,l2,l3):
    cons = []
    dic = {}
    j = 0
    while j < len(l1):
        dic['nombres'] = l1[j]
        dic['apellidos'] = l2[j]
        dic['ciudades'] = l3[j]
        j = j + 1
        cons.append(dic)
        dic = {}
    return cons
nombres = ['esteban', 'ferney', 'gisela','wilfredo','juan']
apellidos = ['quevedo','forero','gomez','moreno','torres']
ciudades = ['bogota','popayan','san gil','merida','bucaramanga']
consolidado = consolidar(nombres,apellidos,ciudades)
print(consolidado)
