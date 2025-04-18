import psycopg2
from config import load_config

def create_phonebook_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        name VARCHAR(50),
        second_name VARCHAR(50),
        phone VARCHAR(20) UNIQUE
    );
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("Таблица 'phonebook' успешно создана!")
    except Exception as e:
        print(" Ошибка при создании таблицы:", e)

if __name__ == '__main__':
    create_phonebook_table()