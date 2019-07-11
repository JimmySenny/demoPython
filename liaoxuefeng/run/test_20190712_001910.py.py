# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    '''
    日期和时间如2015-1-21 9:01:30，时区信息如UTC+5:00，
    将其转换为timestamp
    :param dt_str:
    :param tz_str:
    :return:timestamp
    '''
    ptt = r'^(UTC)([\+\-]\d{1,2})\:00$'
    tz_s = re.match(ptt, tz_str).groups()
    # print(tz_s)
    # print(tz_s[0])
    # print(tz_s[1])

    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    to_tz = timezone(timedelta(hours=int(tz_s[1])))
    dt = cday.replace(tzinfo=to_tz)
    print(dt.timestamp())
    return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
