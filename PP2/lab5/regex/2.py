import re

def function2(s):
    return re.findall(r'ab{2,3}', s)

print(function2("abb"))