"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    count = 1  
    lista1 = []
    lista2 = []
    # SI Primera lista
    if len(s) > 0:
        for _ in s:
            if count % 2 == 0:
                lista1.append('-')
            else:
                lista1.append(str(count))
            count = count + 1           
        # print(lista1)
        return lista1       
    # Si Segunada lista
    if len(s) == 0:        
        lista2.append('0')
        # print(lista2)
        return lista2


