#!/use/bin/env python3
# -*- coding:utf-8 -*-
# 发送图片

import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase

'''
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
'''


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
	           <p><img src="cid:0"></p>
		       </body></html>''';

	msg_all = MIMEMultipart();
	#格式化邮件地址
	msg_all['From'] = _format_addr('Jimmy<%s>' % from_addr);
	#msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
	msg_all['To'] = _format_addr('管理员<%s>' % to_addr);
	msg_all['Subject'] = Header('这是一封来自Python的SMTP问候', 'utf-8').encode();

	msg_all.attach(MIMEText( html, 'html', 'utf-8'));
	with open('./tst.jpg', 'rb' ) as f:
		# 设置附件的MIME和文件名，这里是png类型:
		mime = MIMEBase('image', 'jpg', filename='tst.jpg');
		# 加上必要的头信息:
		mime.add_header('Content-Disposition', 'attachment', filename='tst.jpg')
		mime.add_header('Content-ID', '<0>')
		mime.add_header('X-Attachment-Id', '0')
		# 把附件的内容读进来:
		mime.set_payload(f.read())
		# 用Base64编码:
		encoders.encode_base64(mime)
		msg_all.attach(mime);

	server = smtplib.SMTP(smtp_server, 25);
	server.set_debuglevel(1);
	server.login(from_addr, password);
	server.sendmail(from_addr, [to_addr], msg_all.as_string());
	server.quit();

if __name__ == '__main__':
	main();
