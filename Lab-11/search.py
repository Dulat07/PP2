import psycopg2
from config import load_config

def search_pattern(pattern):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
            for row in cur.fetchall():
                print(f"{row[0]} {row[1]} | {row[2]}")

if __name__ == '__main__':
    p = input(" Введите шаблон для поиска: ")
    search_pattern(p)