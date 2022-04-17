import time
import datetime


ts_now = int(time.time())
print("ts_now int(time.time()): ", ts_now)

ts_local = time.localtime()
print("ts_local: time.localtime()", ts_local)

date = datetime.date(ts_local.tm_year, ts_local.tm_mon, ts_local.tm_mday)
pre = 5 - ts_local.tm_wday
if pre > 0: pre -= 7

nearsat = date +  datetime.timedelta(days=pre)
print("date: {}-{}-{}".format( date.year, date.month, date.day))
print("near Sat", nearsat)



s1 = time.asctime(ts_local)
s2 = time.ctime(ts_now)
print(s1)
print(s2)

time.sleep(1)
s3 = time.strftime("%Y-%m-%d %X")
s4 = time.strftime("%Y-%m-%d %X", ts_local)
print("strftime: ", s3)
print("strftime: ", s4)

# 生成timestamp
time.time()
# 1477471508.05

#struct_time to timestamp
time.mktime(time.localtime())
#生成struct_time
# timestamp to struct_time 本地时间
time.localtime()
time.localtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=16, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

# timestamp to struct_time 格林威治时间
time.gmtime()
time.gmtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=8, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

#format_time to struct_time
time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')
# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)

#生成format_time
#struct_time to format_time
time.strftime("%Y-%m-%d %X")
time.strftime("%Y-%m-%d %X",time.localtime())
# 2016-10-26 16:48:41


#生成固定格式的时间表示格式
time.asctime(time.localtime())
time.ctime(time.time())
# Wed Oct 26 16:45:08 2016