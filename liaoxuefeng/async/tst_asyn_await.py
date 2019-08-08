#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio

async def hello():
	print('Hello Python!');
	r = await asyncio.sleep(2);
	print('Hello Again');

loop = asyncio.get_event_loop();
loop.run_until_complete(hello());
loop.close();
