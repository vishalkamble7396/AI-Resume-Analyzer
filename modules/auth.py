from database.database import conn, cursor

def register(fullname, email, password):
    try:
        cursor.execute(
            "INSERT INTO users(fullname,email,password) VALUES(?,?,?)",
            (fullname, email, password)
        )
        conn.commit()
        return True
    except:
        return False


def login(email, password):
    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )
    return cursor.fetchone()