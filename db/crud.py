import psycopg2
from db.connection import Connection
from models.user import User

def add_roblox_user(user: User) -> None:
    conn = Connection().connect()

    try:
        with conn.cursor() as cur:
            dict = user.to_dict()
            cur.execute(
                f"INSERT INTO {user.table_name} (user_id, is_cpu, username) VALUES (%s, %s, %s)",
                (dict["user_id"], dict["is_cpu"], dict["username"])
            )

        conn.commit()
    except Exception as e:
        print("DB insert error:", e)




