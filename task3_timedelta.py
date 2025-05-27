from datetime import datetime, timedelta

now = datetime.now()
delta = timedelta(days=5)
future_date = now + delta

print("Дата через 5 дней:", future_date.strftime("%Y-%m-%d"))
