"""
이메일을 보내면 이메일을 보냈다라고 True를 출력해주는 
send_email() 메서드를 가진 Email 클래스를 작성하시오.
my_email = Email()
my_email.is_sent # ===> False
my_email.send_email()
my_email.is_sent # ===> True
"""

class Email:

    def __init__(self):
        self.is_sent = False
        print(self.is_sent)

    def send_email(self):
        self.is_sent = True
        return print(self.is_sent)


my_email = Email()
my_email.is_sent
my_email.send_email()
my_email.is_sent