# Создать словарь оценок предполагаемых студентов
# (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.


Students = {
    'Иванов': [2, 3, 5, 3],
    'Петров': [4, 5, 5],
    'Сидоров': [4, 4, 4],
    'Смирнов': [5, 2, 4, 5]
}


def avg(o):
    return sum(o) / len(o)


StudentsAvg = {}
for key in Students:
    val = avg(Students[key])
    StudentsAvg[key] = val

result = {k: v for k, v in sorted(StudentsAvg.items(), key=lambda kv: kv[1])}

print(result)

print("Худший %s" % list(result.keys())[0])

print("Лучший %s" % list(result.keys())[-1])
