import sqlite3
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta


db = sqlite3.connect("db\\bot_db.db")
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
    cursor.execute("INSERT INTO user (user_id, username, full_name, join_date, last_message) VALUES (?, ?, ?, ?, ?)", (user_id, "-" if username is None else username, full_name, date_time, date_time))
    db.commit()

def get_data_from_user(user_id:int) -> list:
    cursor.execute("SELECT * FROM user WHERE user_id = (?)", (user_id,))
    return cursor.fetchone()[1:]

def add_last_message(user_id:int) -> None:
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    cursor.execute("UPDATE user SET last_message = (?) WHERE user_id = (?)", (date_time, user_id))
    db.commit()

def get_all_user_id() -> list:
    cursor.execute("SELECT user_id FROM user")
    return cursor.fetchall()

def count_all_bot_users() -> int:
    cursor.execute("SELECT user_id FROM user")
    return len(cursor.fetchall())

def count_active_bot_users(last_or_join:str) -> int:
    # в течении суток
    cursor.execute(f"SELECT {'last_message' if last_or_join == 'l' else 'join_date'} FROM user")
    data = cursor.fetchall()
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    date_now = date_time.split()[0].split(".")
    time_now = int(date_time.split()[1].split(":")[0])
    count = 0
    for i in data:
        date_last = i[0].split()[0].split(".")
        time_last = int(i[0].split()[1].split(":")[0])
        if int(date_now[1]) - int(date_last[1]) not in [0, 1]:
            continue
        elif date_now[0] == date_last[0] and date_now[1:] == date_last[1:]:
            count += 1
        elif (int(date_now[0]) - int(date_last[0])) == 1 and date_now[1:] == date_last[1:]:
            hour = 24 - time_last
            hour += time_now
            if hour <= 24:
                count += 1
            else:
                continue
    return count

def count_recently_bot_users(last_or_join:str) -> int:
    # в течении последнего часа
    cursor.execute(f"SELECT {'last_message' if last_or_join == 'l' else 'join_date'} FROM user")
    data = cursor.fetchall()
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_time = f"{t.day:02}.{t.month:02}.{t.year:04} {t.hour:02}:{t.minute:02}:{t.second:02}"
    date_now = [int(i) for i in date_time.split()[0].split(".")]
    time_now = int(date_time.split()[1].split(":")[0])
    count = 0
    for i in data:
        date_last = [int(i) for i in i[0].split()[0].split(".")]
        time_last = int(i[0].split()[1].split(":")[0])
        if date_now == date_last:
            if time_now - time_last <= 1:
                count += 1
        elif date_now[0] - date_last[0] == 1 and date_now[1:] == date_last[1:]:
            if time_last == 23 and time_now == 0:
                count += 1
    return count

def count_time_in_bot(user_id:int) -> list:
    # время в боте
    cursor.execute("SELECT join_date FROM user WHERE user_id = (?)", (user_id,))
    data = cursor.fetchone()[0]
    t = datetime.now(pytz.timezone('Europe/Moscow'))
    date_last = data.split()[0].split(".")
    time_last = data.split()[1].split(":")
    dt = datetime(int(date_last[2]), int(date_last[1]), int(date_last[0]), int(time_last[0]), int(time_last[1]), int(time_last[2]), tzinfo=pytz.timezone('Europe/Moscow'))
    rel = relativedelta(t, dt)
    return [rel.years*12+rel.months, rel.days, rel.hours, rel.minutes]

def update_send_start(user_id:int, value:int) -> None:
    cursor.execute("UPDATE user SET send_start = (?) WHERE user_id = (?)", (value, user_id))
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
