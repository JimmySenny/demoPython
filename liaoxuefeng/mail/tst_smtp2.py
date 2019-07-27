#!/use/bin/env python3
# -*- coding:utf-8 -*-
#格式化邮件地址及发送html

import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

def _format_addr(s):
	name, addr = parseaddr(s);
	return formataddr(( Header(name, 'utf-8').encode(), addr ));

def main():
	from_addr = input('From:');
	password = input('Password:');
	to_addr = input('To:');
	smtp_server = input('SMTP server:');
	'''
	text = input('Text:');
	msg = MIMEText( text, 'plain', 'utf-8');
	'''
	html = r'''<html><body><h1>Hello</h1> 
	           <p>send by <a href="http://www.python.org">Python</a>...</p>
		       </body></html>''';
	msg = MIMEText( html, 'html', 'utf-8');

	#格式化邮件地址
	msg['From'] = _format_addr('Jimmy<%s>' % from_addr);
	#msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
	msg['To'] = _format_addr('管理员<%s>' % to_addr);
	msg['Subject'] = Header('这是一封来自Python的SMTP问候', 'utf-8').encode();

	server = smtplib.SMTP(smtp_server, 25);
	server.set_debuglevel(1);
	server.login(from_addr, password);
	server.sendmail(from_addr, [to_addr], msg.as_string());
	server.quit();

if __name__ == '__main__':
	main();
