from datetime import datetime, timedelta

today = datetime.now().date()
tomorrow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)


print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)