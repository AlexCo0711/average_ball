grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # список оценок студентов
students = {'Johnny', 'Bilbo', "Steve", 'Khendrik', 'Aaron'}  # множество студентов
aver_ball = [sum(balls) / len(balls) for balls in grades]  # подсчет среднего балла каждого элемента матрицы grades
spisok = sorted(students)  # сортировка по возрастанию множества students
uspev = dict(zip(spisok, aver_ball))  # создание словаря из множества spisok (ключ) и значений aver_ball
print(uspev) # вывод списка