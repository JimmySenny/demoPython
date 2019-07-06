# -*- coding: utf-8 -*-

import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
'''
If ensure_ascii is True (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is False, these characters will be output as-is.
如果ensure_ascii为True(默认值)，则输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。
'''
print(s)
