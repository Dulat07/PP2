import psycopg2
from config import load_config

def get_page(limit, offset):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
                rows = cur.fetchall()
                print(f"\n Показаны записи с {offset + 1} по {offset + len(rows)}:\n")
                for row in rows:
                    print(f" {row[0]} {row[1]} — {row[2]}")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    limit = 2
    offset = 0

    while True:
        get_page(limit, offset)
        cmd = input("\n[n]ext / [p]rev / [q]uit: ").strip().lower()

        if cmd == 'n':
            offset += limit
        elif cmd == 'p' and offset >= limit:
            offset -= limit
        elif cmd == 'q':
            print(" Выход.")
            break
        else:
            print(" Неверная команда.")