from Lesson18.app import Candidate

class Employee:

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.validate_email()
        self.save_email()



    def save_email(self):
        with open("emails.txt", "a+") as file:
            file.write(self.mail + '\n')

    def validate_email(self):
        with open("emails.txt", "r") as file:
            if self.mail in file.read():
                raise ValueError('Email is already in use.')


vasya = Employee(name='Vasya', mail='123@1.com')
petya = Employee(name='Petya', mail='1234@1.com')
marina = Employee(name='Marina', mail='12345@1.com')

