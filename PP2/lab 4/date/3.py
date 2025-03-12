from datetime import datetime 

now = datetime.now()
without_microsecond = now.replace(microsecond=0)

print(now)
print(without_microsecond)