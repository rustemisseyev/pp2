import re

def function8(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

print(function8("HelloWorldTest"))