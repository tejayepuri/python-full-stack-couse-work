'''from datetime import date,time,datetime
today=date.today()
print(today)

print(date(2026,3,31))

print("year:",today.year)
print("Month:",today.month)
print("day:",today.day)
print(today.weekday())
print(today.isoweekday())'''

'''from datetime import date,time,datetime
now=time(21,56,18)
print(now)

print(now.hour)
print(now.minute)
print(now.second)'''

'''from datetime import date,time,datetime
now=datetime.now()
print(now)'''

'''from datetime import date,time,datetime     #convert date and time into string
now=datetime.now()
print(now.strftime('%d %m %y %H %M'))
print(now.strftime('%d %m %y %I %M %S'))'''


from datetime import date,datetime,timedelta
today=date.today()
now=datetime.now()

today_7=today-timedelta(days=7)
print(today_7)

now_30=now+timedelta(minutes=30)
print(now_30)

