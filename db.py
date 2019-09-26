def init_db():
    """データベースの初期化を行う関数"""
    import sqlite3

    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    with open("schema.sql", mode="r", encoding="utf-8") as f:
        sql = f.read()

    cursor.executescript(sql)

    conn.commit()

    conn.close()


def find_all_users():
    import sqlite3

    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM customers"

    results = conn.execute(sql)

    users = results.fetchall()

    conn.commit()

    conn.close()

    return users

if __name__ == "__main__":
    init_db()
