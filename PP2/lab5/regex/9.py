import re

def function9(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(function9("HelloWorldTest"))