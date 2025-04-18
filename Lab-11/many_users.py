import psycopg2
import csv
from config import load_config

def insert_many_users_from_csv(filename):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute("CALL insert_user_if_valid(%s, %s, %s);",
                                    (row['name'].strip(), row['second_name'].strip(), row['phone'].strip()))
        print("Все пользователи обработаны.")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    insert_many_users_from_csv("contacts.csv")