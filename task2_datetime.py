from datetime import datetime

now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
day_of_week = now.strftime("%A")
week_number = now.isocalendar()[1]

print("Текущая дата и время:", formatted)
print("День недели:", day_of_week)
print("Номер недели в году:", week_number)

