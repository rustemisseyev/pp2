from datetime import datetime, timedelta

today_date = datetime.now()
new_date = today_date - timedelta(days=5)

print(new_date.strftime("%Y/%m/%d"))