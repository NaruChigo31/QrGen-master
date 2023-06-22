import datetime

lastpayment = datetime.datetime(2022,8,8)
date = datetime.datetime.now()
if (lastpayment.month < date.month and date.day == lastpayment.day and lastpayment.year <= date.year) or (lastpayment.month < date.month and date.day > lastpayment.day) or (lastpayment.year < date.year):
  print("Просрочено")
else:
  print("Норм")
