import mysql.connector as mysql
import Creds
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)

cursor = db.cursor(dictionary=True)
cursor.execute('''
    SELECT
        s.name AS student_name,
        s.second_name AS second_name,
        g.title AS group_title,
        b.title AS book_title,
        sb.title AS subject_title,
        m.value AS mark_value,
        l.title AS lesson_title
    FROM books AS b
    INNER JOIN students AS s ON b.taken_by_student_id = s.id
    INNER JOIN `groups` AS g ON s.group_id = g.id
    INNER JOIN marks AS m ON m.student_id = s.id
    INNER JOIN lessons AS l ON m.lesson_id = l.id
    INNER JOIN subjects AS sb ON sb.id = l.subject_id''')

db_data = cursor.fetchall()

base_path = os.path.dirname(os.path.abspath(__file__))
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

csv_data = []
with open(file_path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_data.append(dict(row))

missing_list = []
for csv_row in csv_data:
    mapped_row = {
        "student_name": csv_row["name"],
        "second_name": csv_row["second_name"],
        "group_title": csv_row["group_title"],
        "book_title": csv_row["book_title"],
        "subject_title": csv_row["subject_title"],
        "lesson_title": csv_row["lesson_title"],
        "mark_value": csv_row["mark_value"]
    }
    if mapped_row not in db_data:
        missing_list.append(mapped_row)

print(missing_list)
