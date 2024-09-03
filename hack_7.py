"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    lista1 = []
    lista2 = []
    i = 0
    if isinstance(s[i], str):
        i = 1
        while i-1 < len(s):
            if i % 2 == 0:
                lista1.append(i)
            else:
                lista1.append(f'{i}')
            i +=1    
        return lista1
    else:
        lista2.append(s[i])
        return lista2
