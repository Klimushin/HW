# Создать структуру данных для студентов 
# из имен и фамилий, можно случайных. 
# Придумать структуру данных, чтобы указывать, 
# в какой группе учится студент (Группы Python, 
# FrontEnd, FullStack, Java). Студент может 
# учиться в нескольких группах. Затем вывести:
# - студентов, которые учатся в двух и более группах
# - студентов, которые не учатся на фронтенде
# - студентов, которые изучают Python или Java

groupPython = {
    'Signe Whitehair',
    'Zackary Stegner',
    'Bart Jenney',
    'Annamae Cannaday',
    'Lady Sylvia',
    'Yasmine Roseboro',
    'Walton Milazzo',
}
groupFrontend = {
    'Claretha Purington',
    'Vergie Holtz',
    'Walton Milazzo',
}
groupJava = {
    'Signe Whitehair',
    'Zackary Stegner',
    'Bart Jenney',
    'Yasmine Roseboro',
    'Walton Milazzo',
}
groupFullStack = {
    'Claretha Purington',
    'Vergie Holtz'
}

programmers = groupFrontend | groupJava | groupPython | groupFullStack
print('не фронтенд')
print(programmers - groupFrontend)
print('2+ группы')
print(groupFrontend & groupJava)
print(groupFrontend & groupPython)
print(groupFrontend & groupFullStack)
print(groupPython & groupFullStack)
print(groupPython & groupJava)
print(groupJava & groupFullStack)
print('Python+Java')
print(groupPython & groupJava)
