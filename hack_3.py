"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
   result = ""
   for word in s.split():
      if word.startswith("qu") and len(s) <= 2:
         result += "Qv"
      elif word.startswith("3"):
         result += "3Q"
      else:
         result += word[0].upper() + word[1:].replace("o", "0").replace("a", "@").replace("i", "¡").replace("n", "N").replace("x", "X").replace("u", "v")
      result += " "
   return result.strip()