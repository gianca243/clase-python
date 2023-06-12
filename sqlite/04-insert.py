import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        INSERT into usuarios values(?, ?)
        """,
        (1, "hola mundo"),
    )
