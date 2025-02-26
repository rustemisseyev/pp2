import re

def function10(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

print(function10("HelloWorldTest"))