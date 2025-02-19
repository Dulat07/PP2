from datetime import datetime , timedelta

data1 = datetime.now().replace(microsecond=0)
data2 = timedelta( days = 1, hours=4, minutes=35, seconds=46)

difference = data1 - data2

print(difference)