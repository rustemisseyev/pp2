import re

def function4(s):
    return re.findall(r'\b[A-Z][a-z]+', s)

print(function4("Hello World Test"))