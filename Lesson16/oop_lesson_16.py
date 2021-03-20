from datetime import date, timedelta


class Employee:

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, mail, salary):
        self.name = name
        self.mail = mail
        self.salary = salary
        # self.days = days

    def work(self):
        return f'I come to the office.'

    def day(self):
        day_count = 0
        now = date.today()
        month_start = date(now.year, now.month, 1)

        weekend = [5, 6]

        diff = (now - month_start).days + 1

        # print(now, month_start, diff)

        day_count = 0

        for day in range(diff):
            # print((month_start + timedelta(day)).weekday())
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return day_count

    def check_salary(self, salary):
        day = self.day()
        salary = self.salary * day
        return salary


class Recruiter(Employee):
    def work(self):
        return f'I come to the office and start to hiring.'

    def __str__(self):
        return f" {self.__class__} | name: {self.name}"


class Programmer(Employee):
    def work(self):
        return f'I come to the office and start to coding.'

    def __str__(self):
        return f"{self.__class__} | name: {self.name}"


if __name__ == '__main__':
    vasya = Recruiter(name='Vasya', mail='123@1.com', salary=50)
    vasya2 = Programmer(name='Vasya2', mail='1234@1.com', salary=50)
    marina = Programmer(name='marina', mail='12345@1.com', salary=60)
    salary_Vasya2 = vasya2.check_salary(50)
    print(salary_Vasya2)
    print(str(vasya2.check_salary))
    print(marina.work())
