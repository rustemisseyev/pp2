import re

def function3(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

print(function3("hello_world test_example"))