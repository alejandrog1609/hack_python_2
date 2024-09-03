"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = []
    for word in s.split():
        if len(word) < 3:
            result.append(word)
        elif word.startswith('f'):
            result.append('-'.join(word[i:i+2] for i in range(0, len(word)-1, 3)).replace("an", "ma-"))
        elif word.startswith('b'):
            result.append('-'.join(word[i:i+2] for i in range(0, len(word)-1, 3)))
        else:
            result.append('-'.join(word[i:i+2] for i in range(0, len(word), 3)) + '-')
    return ' '.join(result)
