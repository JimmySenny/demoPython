# -*- coding: utf-8 -*-
import re
def name_of_email(addr):
    '''
    提取出带名字的Email地址的前面用户名：
    <Tom Paris> tom@voyager.org => Tom Paris
    bob@example.com => bob
    :param addr
    :return: name
    '''

    name = ''
    re_email_name = re.compile(r'^([\<\w\s\>]*)\@\w+\.\w+$');
    m = re_email_name.match(addr)
    if(m):
        if '<' in m.group(1):
            name = re.split(r'[\<\>]', m.group(1))[1];
        else:
            name = m.group(1)
        return name

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
