import re

def function1(s):
    return re.findall(r'ab*', s)

print(function1("abbb"))