#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#发送纯文本邮件

import smtplib, email
from email.mime.text import MIMEText

def msg():
	#第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'
	return MIMEText('hello! send by python', 'plain', 'utf-8');

def main():
	#输入相关信息
	from_addr = input('From:');
	password = input('Password:');
	to_addr = input('To:');
	smtp_server = input('SMTP SERVER:');
	text = input('TEXT:');
	msg = MIMEText( text, 'plain', 'utf-8');

	server = smtplib.SMTP(smtp_server, 25); #SMTP协议默认端口是25
	server.set_debuglevel(1);
	server.login(from_addr, password);
	server.sendmail(from_addr, [to_addr], msg.as_string());
	server.quit();

if __name__ == '__main__':
	main();
