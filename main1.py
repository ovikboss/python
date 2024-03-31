import smtplib
from email.mime.text import MIMEText

def send_email(massage):
    sender="bloodysimonyan@yandex.ru"
    password="Simonyan99"
    server=smtplib.SMTP("smtp.yandex.ru",587)
    server.starttls()

    try:
      server.login(sender,password)
      msg=MIMEText(massage)
      msg["Subject"]="Тема сообщения"
      print(massage)
      server.sendmail(sender,"ovikboss2016@gmail.com",msg.as_string())
    
    except Exception as _ex  :
      return f"{_ex}\nCheck your login or password"
    
def main():
       massage= input("Введите свое сообщение: ")
       print(send_email(massage=massage))

print("Start")
main()
    