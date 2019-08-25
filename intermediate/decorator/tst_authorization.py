#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import wraps

def requires_auth(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			authenticate();
		return func(*args, **kwargs);
	return decorated;


