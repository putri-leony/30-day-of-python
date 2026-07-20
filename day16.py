>>> import datetime
>>> print(dir(datetime))
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now)
2026-07-08 10:50:18.217983
>>> day = now.day
>>> print(day)
8
>>> month = now.month
>>> year = now.year
>>> timestamp = now.timestamp()
>>> print(timestamp)
1783482618.217983
>>> print(day,month,year)
8 7 2026
>>> hour = now.hour
>>> minute = now.minute
>>> second = now.second
>>> print(f'{day}/{month}/{year}, {hour}:{minute}')
8/7/2026, 10:50
>>> from datetime import date
>>> d = date(2020,1,1)
>>> print(d)
2020-01-01
>>> print('Current date:', d.today())
Current date: 2026-07-08
>>> today = date.today()
>>> print(today)
2026-07-08
>>> print('Current year:', today.year)
Current year: 2026
>>> from datetime import time
>>> a = time()
>>> print('a=', a)
a= 00:00:00
>>> b = time(10,30,50)
>>> print('b=', b)
b= 10:30:50
>>> c = time(hour=10, minute=30, second=50)
>>> print('c=', c)
c= 10:30:50
>>> from datetime import timedelta
>>> t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
>>> t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
>>> t3 = t1-t2
>>> print('t3:', t3)
t3: 86 days, 22:56:50
