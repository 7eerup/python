from smtplib import SMTP_SSL
from email.message import EmailMessage

# 이메일 메시지 설정
msg = EmailMessage()
msg['Subject'] = 'E-mail 자동화 전송'
msg['From'] = '7eerup@gmail.com'
msg['To'] = '7eerup@naver.com'
msg.set_content('This is a test email.')

# SMTP 설정 및 이메일 전송
with SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # 서버 로그인
    smtp.login('메일 주소', '앱 비밀번호')
    smtp.send_message(msg)

print("성공!")