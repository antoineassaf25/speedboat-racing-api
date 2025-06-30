import psycopg2
from db.connection import Connection
from models.user import User
from models.api_user import APIUser
import bcrypt

def add_roblox_user(user: User) -> None:
    conn = Connection().connect()

    try:
        with conn.cursor() as cur:
            user_data = user.to_dict()
            target_table = user.table_name
            cur.execute(
                f"""
                INSERT INTO {target_table} (user_id, is_cpu, username)
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id) DO NOTHING
                """,
                (user_data["user_id"], user_data["is_cpu"], user_data["username"])
            )

        conn.commit()
    except Exception as e:
        conn.rollback()
        print("DB insert error:", e)

def check_api_user_admin(api_user: APIUser, plain_password: str) -> bool:
    conn = Connection().connect()

    try: 
        with conn.cursor() as cur:
            api_user_data = api_user.to_dict()
            target_table = api_user.table_name

            cur.execute(
                f"""
                SELECT password_hash, role
                FROM {target_table}
                WHERE username = %s
                """,
                (api_user_data["username"],)
            )

            result = cur.fetchone()

            # check if user is found
            if result is None:
                return False

            matching = bcrypt.checkpw(plain_password.encode(), result[0].encode())
            print(matching)

            return matching and result[1].lower() == "admin"

    except Exception as e:
        conn.rollback()
        print("DB retrieval error:", e)

def register_user(api_user: APIUser) -> None:
    conn = Connection().connect()

    try:
        with conn.cursor() as cur:
            api_user_data = api_user.to_dict()
            target_table = api_user.table_name

            cur.execute(
                f"""
                INSERT INTO {target_table} (username, password_hash, role)
                VALUES (%s, %s, %s)
                ON CONFLICT (username) DO NOTHING
                """,
                (api_user_data["username"], api_user_data["password_hash"], api_user_data["role"])
            )

        conn.commit()  
        return True         

    except Exception as e:
        conn.rollback()
        print("Unable to register user:", e)
        return False





