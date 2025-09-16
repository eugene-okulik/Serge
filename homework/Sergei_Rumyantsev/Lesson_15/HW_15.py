import mysql.connector as mysql
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Задание 1: Создайте студента (student)
student_query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
student_values = ('Serge', 'Rumyantsev')
cursor.execute(student_query, student_values)
student_id = cursor.lastrowid
cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
print(cursor.fetchone())

# Задание 2: Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
book_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
book_values = [
    ('Граф Монте-Кристо', student_id),
    ('Ревизор', student_id),
    ('Герои нашего времени', student_id),
    ('Преступление и наказание', student_id)
]
cursor.executemany(book_query, book_values)
cursor.execute(f'SELECT * FROM books WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

# Задание 3: Создайте группу (group) и определите своего студента туда
start_date = datetime.now()
end_date = start_date + relativedelta(years=1)
group_query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
group_values = ('Serge_group', start_date.strftime("%Y %B %d"), end_date.strftime("%Y %B %d"))
cursor.execute(group_query, group_values)
student_group_id = cursor.lastrowid

cursor.execute(f'UPDATE students SET group_id = {student_group_id} WHERE id = {student_id}')

cursor.execute(f'SELECT * FROM `groups` WHERE id = {student_group_id}')
print(cursor.fetchall())

cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
print(cursor.fetchall())

# Задание 4: Создайте несколько учебных предметов (subjects)
subjects_query = 'INSERT INTO subjects (title) VALUES (%s)'
subjects_values = [
    ('For_test_Math'),
    ('For_test_PE'),
    ('For_test_Foreing_lang'),
    ('For_test_Foreing_History')
]
subjects_id = []
for value in subjects_values:
    cursor.execute(subjects_query, (value,))
    subjects_id.append(cursor.lastrowid)

for id in subjects_id:
    cursor.execute(f'SELECT * FROM subjects WHERE id = {id}')
    print(cursor.fetchall())

# Задание 5: Создайте по два занятия для каждого предмета (lessons)
lessons_query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
lessons_values = []
lessons_id = []


for subject, subj_id in zip(subjects_values, subjects_id):
    subj_list = subject.split('_')
    subj_name = ' '.join(subj_list[2:])

    for lesson_num in range(2):
        lesson_res = f"{subj_name}_{lesson_num}"
        lessons_values.append((lesson_res, subj_id))

for value in lessons_values:
    cursor.execute(lessons_query, value)
    lessons_id.append(cursor.lastrowid)

for id in lessons_id:
    cursor.execute(f'SELECT * FROM lessons WHERE id = {id}')
    print(cursor.fetchall())


# Задание 6: Поставьте своему студенту оценки (marks) для всех созданных вами занятий
marks_query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
marks_id = []

for id in lessons_id:
    mark = random.randint(2, 5)
    value = (mark, id, student_id)
    cursor.execute(marks_query, value)
    marks_id.append(cursor.lastrowid)

for id in marks_id:
    cursor.execute(f'SELECT * FROM marks WHERE id = {id}')
    print(cursor.fetchall())

# Задание 7_1: Все оценки студента
cursor.execute(f'SELECT value FROM marks m WHERE m.student_id = {student_id}')
print(cursor.fetchall())

# Задание 7_2: Все книги, которые находятся у студента
cursor.execute(f'SELECT title FROM books b WHERE b.taken_by_student_id = {student_id}')
print(cursor.fetchall())

# Задание 7_3: Для вашего студента выведите всё, что о нем есть в базе:
# группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
cursor.execute(f'''
    SELECT
        s.name AS student_name,
        g.title AS group_title,
        b.title AS book_title,
        m.value AS mark_value,
        l.title AS lesson_title,
        sb.title AS subject_title
    FROM books AS b
    INNER JOIN students AS s ON b.taken_by_student_id = s.id
    INNER JOIN `groups` AS g ON s.group_id = g.id
    INNER JOIN marks AS m ON m.student_id = s.id
    INNER JOIN lessons AS l ON m.lesson_id = l.id
    INNER JOIN subjects AS sb ON sb.id = l.subject_id
    WHERE s.id = {student_id}''')
print(cursor.fetchall())

db.commit()

db.close()
