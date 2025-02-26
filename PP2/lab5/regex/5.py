import re

def function5(s):
    return re.findall(r'a.*b', s)

print(function5("axyzb"))