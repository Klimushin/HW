from Lesson18.models import Recruiter, Programmer, Employee


class Candidate(Employee):
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
        self.work()

    def UnableToWorkException(self):
        try:
            self.work() != 1
        except self.UnableToWorkException():
            return "I’m not hired yet, lol."


class Vacancy(Employee):
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


if __name__ == '__main__':
    vasya = Recruiter(name='Vasya', mail='123@1.com', salary=50)
    vasya2 = Programmer(name='Mitia', mail='1234@1.com', salary=50, tech_stack=1)
    marina = Programmer(name='marina', mail='12345@1.com', salary=60, tech_stack=3)
    petya = Candidate(full_name='Petya', email='3548@1.com', technologies=2, main_skill=4, main_skill_grade=7)

    # Candidate.work()
    print(petya.UnableToWorkException())
    # salary_Vasya2 = vasya2.check_salary(50)
    # print(salary_Vasya2)
    # print(str(vasya2.check_salary))
    # print(marina.work())
