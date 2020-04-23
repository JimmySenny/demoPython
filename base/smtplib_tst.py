from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = 'jimmysheng128@126.com';
    receivers = [ 'jimmysenny@126.com'];
    message = MIMEText('请周一完成周例会', 'plain', 'utf-8');
    message['From'] = Header('Jimmy', 'utf-8');
    message['To'] = Header('Senny', 'utf-8' );
    message['Subject'] = Header('周一工作安排', 'utf-8');
    smtper = SMTP('smtp.126.com');
    
    smtper.sendmail(sender,receivers, message.as_string());

    print('send done');

if __name__ == '__main__':
    main();
