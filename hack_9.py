"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
  result = {}
  for clave, valor in s.items():
    if clave == "foo":
      valor = valor.replace("k", "")
      result["Foo"] = valor.capitalize()
  return result

