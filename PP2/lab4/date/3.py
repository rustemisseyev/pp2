from datetime import datetime

current_time = datetime.now().replace(microsecond=0)

print("Current Time without Microseconds:", current_time)