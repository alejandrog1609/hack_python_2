"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
   listas = s
   result = []
   i = 0
   for i, x in enumerate(reversed(s), start=0):
         if len(listas) % 2 != 0:
            content = f"{x}-{len(s) - i}" 
            result.append(content)
         elif len(listas) % 2 == 0:
            content = f"{i+1}"
            result.append(content)
            result.sort(reverse=True)
            i += 1
   return result
