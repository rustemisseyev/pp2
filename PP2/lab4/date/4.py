from datetime import datetime

a = datetime(2024, 2, 1, 12, 0, 0) 
b = datetime(2024, 2, 10, 14, 30, 0) 

c = abs((b - a).total_seconds())

print(c)