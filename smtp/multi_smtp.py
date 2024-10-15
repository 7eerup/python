from smtplib import SMTP_SSL
from email.message import EmailMessage

customer_list = [
    '받는 사람 주소1',
    '받는 사람 주소2',
    '받는 사람 주소3'
]

# 이메일 메시지 설정
for customer in customer_list:
    msg = EmailMessage()
    msg['Subject'] = 'E-mail 자동화 전송'
    msg['From'] = '7eerup@gmail.com'
    msg['To'] = customer_list
    msg.set_content('This is a test email.')

# SMTP 설정 및 이메일 전송
with SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('메일 주소', '앱 비밀번호')
    smtp.send_message(msg)

print("성공!")