import sqlite3
from aiogram import Bot
import config as cf

async def add_user(usid: int, subscribe: str, date: str) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """INSERT INTO Users (user_id, subscribe, datesubscribe) VALUES (?, ?, ?)"""
        cursor.execute(query, (usid, subscribe, date))
        db.commit()


async def seach_user(usid: int):
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """SELECT * FROM Users WHERE user_id = ?;"""
        cursor.execute(query, (usid,))
        data = cursor.fetchall()
        db.commit()
        return data


async def seach_profi(usid: int):
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """SELECT * FROM Profies WHERE user_id = ?;"""
        cursor.execute(query, (usid,))
        data = cursor.fetchall()
        db.commit()
        print(data)
        return data


async def seach_Pro(city: str, self_cat: str, self_subcat: str):
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """SELECT user_name, full_name FROM Profies WHERE chat_city = ? AND self_cat = ? AND self_subcat = ?;"""
        cursor.execute(query, (city, self_cat, self_subcat))
        data = cursor.fetchall()
        db.commit()
        print(data)
        return data


async def check_user(usid: int, bot: Bot):
    res = await seach_user(usid)
    print(res)
    if not res:
        await add_user(usid, "Base", "0")
        await bot.send_message(cf.ADMIN_ID, f"Новый пользователь с айди -> {usid} зашел в чат")
        return "user"
    res = await seach_profi(usid)
    print(res)
    if not res:
        return "user"
    else:
        return "profi"


async def add_profi(user_name: str, user_id: int, full_name: str, city: str, chat_city: str, phone: str, self_cat: str,
                    self_subcat: str, promo_link: str, price: str) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """INSERT INTO Profies 
        (user_id, user_name, full_name, city, chat_city, self_cat, self_subcat, phone, promo_link, price) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (
        user_id, user_name, full_name, city, chat_city, self_cat, self_subcat, phone, promo_link, price))
        db.commit()


async def update_profi_phone(phone, usid) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """UPDATE Profies SET phone = ? WHERE user_id = ?;"""
        cursor.execute(query, (phone, usid))
        db.commit()

async def update_profi_fullname(full_name, usid) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """UPDATE Profies SET full_name = ? WHERE user_id = ?;"""
        cursor.execute(query, (full_name, usid))
        db.commit()


async def update_profi_city(city, usid) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """UPDATE Profies SET city = ? WHERE user_id = ?;"""
        cursor.execute(query, (city, usid))
        db.commit()




async def seach_user_all():
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """SELECT user_id FROM Users"""
        cursor.execute(query)
        data = cursor.fetchall()
        db.commit()
        return data


async def update_profi_promo_link(promo_link, id) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """UPDATE Profies SET promo_link = ? WHERE id = ?;"""
        cursor.execute(query, (promo_link, id))
        db.commit()


async def update_profi_price(price, id) -> None:
    with sqlite3.connect("db.sqlite3") as db:
        cursor = db.cursor()
        query = """UPDATE Profies SET price = ? WHERE id = ?;"""
        cursor.execute(query, (price, id))
        db.commit()