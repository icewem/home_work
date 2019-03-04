from datetime import datetime, timedelta,date

check_day = [0,1,30]

for check_data in check_day:
  print_result = date.today() - timedelta(days=check_data)
  print(print_result.strftime('%d %B %Y'))