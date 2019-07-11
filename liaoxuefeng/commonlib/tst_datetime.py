#!/usr/bin/env python3
# -*- conding:utf-8 -*-

# 如果仅导入import datetime，则必须引用全名datetime.datetime
from datetime import datetime, timedelta, timezone


def tst_now():
	now = datetime.now(); #获取当前datetime
	print(now);
	print(type(now)); # <class 'datetime.datetime'>

def tst_datetime():
	dt = datetime(2015, 4, 19, 12, 20); # 用指定日期时间创建datetime
	print(dt);

def tst_dt2ts():
	dt = datetime(2015, 4, 19, 12, 20);
	ts = dt.timestamp();
	print(ts);

def tst_ts2dt():
	t = 1429417200.0;
	dt = datetime.fromtimestamp(t);
	print(dt);
	dt_utc = datetime.utcfromtimestamp(t);
	print(dt_utc);

def tst_str2dt():
	cday = datetime.strptime('2019/07/10 12:13:14', '%Y/%m/%d %H:%M:%S');
	print(cday);
	print(type(cday));

def tst_dt2str():
	now = datetime.now();
	s = now.strftime('%a, %b, %d %H:%M');
	print(s);
	print(type(s));

def tst_timedelta():
	now = datetime.now();
	print(now);
	print(now + timedelta(hours=10));
	print(now + timedelta(days=1));
	print(now + timedelta(days=1, hours=12));

def tst_timezone():
	now = datetime.now();
	print(now);
	tz_utc8 = timezone(timedelta(hours=9)); # 创建时区UTC+8:00
	dt = now.replace(tzinfo=tz_utc8); # 强制设置为UTC+8:00
	print(dt);

def tst_utcnow_astimezone():
	# 拿到UTC时间，并强制设置时区为UTC+0:00:
	utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc);
	print(utc_dt);
	# astimezone()将转换时区为北京时间:
	utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)));
	print(utc8_dt);
	utc9_dt = utc8_dt.astimezone(timezone(timedelta(hours=9)));
	print(utc9_dt);

def main():
	tst_now();
	tst_datetime();
	tst_dt2ts();
	tst_ts2dt();
	tst_str2dt();
	tst_dt2str();
	tst_timedelta();
	tst_timezone();
	tst_utcnow_astimezone();

if __name__ == '__main__':
	main();
