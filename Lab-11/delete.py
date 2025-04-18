import psycopg2
from config import load_config

def delete_user():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                print(" Удаление из PhoneBook")
                name = input("Введите имя (или нажмите Enter, чтобы пропустить): ").strip()
                phone = input("Введите номер телефона (или нажмите Enter, чтобы пропустить): ").strip()

                if not name and not phone:
                    print(" Вы должны ввести хотя бы имя или номер телефона.")
                    return

                cur.execute("CALL delete_from_phonebook(%s, %s);", (name if name else None, phone if phone else None))
                print(" Удаление завершено.")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    delete_user()