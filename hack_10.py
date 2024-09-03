"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(s):
  lista = []
  numero = 1
  for diccionario in s:
    dic = {}
    for clave, valor in diccionario.items():
      dic[str(numero)] = str(numero + 1)
      numero += 2
    lista.append(dic)
  return lista
