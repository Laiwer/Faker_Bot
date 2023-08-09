import sqlite3
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta


db = sqlite3.connect("bot_db.db")
cursor = db.cursor()

def existe_in_db(table:str, user_id:int) -> bool:
    cursor.execute(f"SELECT user_id FROM {table}")
    for i in cursor.fetchall():
        if user_id in i:
            return True
    return False



# ?==================================================
# ?|||                   Юзер                     |||
# ?==================================================
def add_user_in_data_base(user_id:int, username:str, full_name:str) -> None:
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    cursor.execute("INSERT INTO user (user_id, username, full_name, join_date, last_message) VALUES (?, ?, ?, ?, ?)", (user_id, username, full_name, date_time, date_time))
    db.commit()

def get_data_from_user(user_id:int) -> list:
    cursor.execute("SELECT * FROM user WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def add_last_message(user_id:int) -> None:
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    cursor.execute("UPDATE user SET last_message = (?) WHERE user_id = (?)", (date_time, user_id))
    db.commit()



# ?==================================================
# ?|||              Местоположение                |||
# ?==================================================
def add_user_in_geolocate(user_id:int) -> None:
    cursor.execute("INSERT INTO geolocate (user_id) VALUES (?)", (user_id,))
    db.commit()

def get_data_from_geolocate(user_id:int) -> list:
    cursor.execute("SELECT * FROM geolocate WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def update_data_in_geolocate(user_id:int, type:str, data) -> None:
    cursor.execute(f"UPDATE geolocate SET {type} = (?) WHERE user_id = (?)", (data, user_id))
    db.commit()