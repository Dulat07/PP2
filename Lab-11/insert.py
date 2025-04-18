import psycopg2
from config import load_config

def upsert_user(name, second_name, phone):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL upsert_phonebook(%s, %s, %s);", (name, second_name, phone))
                print(" Пользователь успешно добавлен или обновлён.")
    except Exception as e:
        print(" Ошибка:", e)

if __name__ == '__main__':
    name = input("Имя: ").strip()
    second_name = input("Фамилия: ").strip()
    phone = input("Телефон: ").strip()
    upsert_user(name, second_name, phone)