'''
string
字串形式表示時間：time.ctime()
datetime
In [15]: datetime.datetime.now()
Out[15]: datetime.datetime(2018, 11, 14, 16, 38, 16, 152438)
time
In [14]: time.localtime()
Out[14]: time.struct_time(tm_year=2018, tm_mon=11, tm_mday=14, tm_hour=16, tm_min=36, tm_sec=18, tm_wday=2, tm_yday=318, tm_isdst=0)
timestamp:
自1970年1月1日(00:00:00 GMT)以來的秒數
In [16]: time.time()
Out[16]: 1542184899.844029

'''
import time
import datetime


print(time.ctime(),type(time.ctime()))
# Sun Sep 27 09:44:09 2020 <class 'str'>
print(time.localtime(),type(time.localtime()))
# time.struct_time(tm_year=2020, tm_mon=9, tm_mday=27, tm_hour=9, tm_min=44, tm_sec=9, tm_wday=6, tm_yday=271, tm_isdst=0) <class 'time.struct_time'>
print(time.time(),type(time.time()))
# 1601171049.9131796 <class 'float'>
print(datetime.datetime.now(),type(datetime.datetime.now()))
# 2020-09-27 09:44:09.913179 <class 'datetime.datetime'>
print(datetime.date.today(),type(datetime.date.today()))
# 2020-09-27 <class 'datetime.date'>


# ts to time and datetime then to string

ts = 1599714530.824476
print(time.localtime(ts))
print(datetime.datetime.fromtimestamp(ts))
print(datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M"))

ts = round(ts)
print(time.localtime(ts))
print(datetime.datetime.fromtimestamp(ts))
print(datetime.datetime.fromtimestamp(ts).strftime("%y-%m-%d %H:%M"))


print((str(datetime.date.today() )))
print((str(datetime.date.today() - datetime.timedelta(days=1)  )))

filename = './pic/{}/'.format(str(datetime.date.today() - datetime.timedelta(days=1)))
print(filename)