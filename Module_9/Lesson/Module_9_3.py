first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(first_string) - len(second_string) for first_string, second_string in zip(first, second)
                if len(first_string) != len(second_string))

# 2. Генераторная сборка для результатов сравнения строк в одинаковых позициях без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))