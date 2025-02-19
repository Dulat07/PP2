from datetime import datetime , timedelta

current_date = datetime.now()
data = current_date + timedelta(days = 5)

print(f"Дата через 5 дней: {data}")
