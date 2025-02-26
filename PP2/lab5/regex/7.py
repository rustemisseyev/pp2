import re

def function7(s):
    return ''.join(word.capitalize() for word in s.split('_'))

print(function7("hello_world_test"))