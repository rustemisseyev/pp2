import re

def function6(s):
    return re.sub(r'[ .,]', ':', s)

print(function6("Hello, World. Test"))