import random

import request
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.filters import BaseFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import keyboard as kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import config as cf
from middleeware import MediaMiddlewareCountClick
import text

router = Router()


class Form(StatesGroup):
    get_fullname = State()
    get_city = State()
    get_selfcat = State()
    get_selfsubcat = State()
    no_city = State()
    phone = State()
    price = State()
    promo_link = State()


class Question(StatesGroup):
    get_question = State()


class UpdateBase(StatesGroup):
    get_id = State()
    get_promo_link = State()
    get_price = State()


class Update(StatesGroup):
    get_fullname = State()
    get_city = State()
    get_phone = State()


class ADMIN(StatesGroup):
    search_user = State()
    advertisement = State()
    user_id = State()


class CityCheck(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.city:
            if callbeck.data == i and i not in currentCity:
                print("yes")
                currentCity.append(i)
                return callbeck.data == i
        else:
            return False


class CityChecksearch(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.city2:
            if callbeck.data == i and i not in currentCity:
                print("yes")
                currentCity.append(i)
                return callbeck.data == i
        else:
            return False


class CatCheck(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.self_cat:
            if callbeck.data == i:
                return callbeck.data == i
        else:
            return False


class CatChecksearch(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.self_cat2:
            if callbeck.data == i:
                return callbeck.data == i
        else:
            return False


class SubCatCheck(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.self_subcat:
            if callbeck.data == i:
                return callbeck.data == i
        else:
            return False


class SubCatChecksearch(BaseFilter):
    async def __call__(self, callbeck: CallbackQuery):
        for i in cf.self_subcat2:
            if callbeck.data == i:
                return callbeck.data == i
        else:
            return False


currentCity = []


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext, bot: Bot):
    currentCity.clear()
    await state.clear()
    res = await request.check_user(message.from_user.id, bot)
    print(message.from_user.id)
    if message.from_user.id == cf.ADMIN_ID:
        await message.answer("Админ панель💻", reply_markup=kb.admin_panel)
    elif res == "user":
        await message.answer("Выберите раздел 👇", reply_markup=kb.startuser_kb)
    else:
        await message.answer("Выберите раздел 👇", reply_markup=kb.startprofi_kb)


@router.callback_query(F.data == "search user")
async def cmd_search_user(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ADMIN.search_user)
    await callback.message.edit_text("🤖Пришлите мне айди пользователя")


@router.message(ADMIN.search_user)
async def get_search_user(message: Message, state: FSMContext):
    try:
        data = message.text
        res = await request.seach_profi(data)
        count = 0
        msg = f"Данные пользователя {data}\nUserName: @<b>{res[0][2]}</b>\nИмя Фамилия: <b>{res[0][3]}</b>\nГород: <b>{res[0][4]}</b>\nТелефон: <b>{res[0][8]}</b>\n"
        for i in res:
            count += 1
            msg += f"<b>{count}.</b>\n"
            text = f"Чат города: {i[5]}\n  Категория: {i[6]}\n  Подкатегория: {i[7]}\n  Ссылка на промо: {i[9]}\n  Стоимость услуг: {i[10]}\n"
            msg += text
        await message.answer(msg, parse_mode="HTML")
    except Exception:
        await message.answer("Не найденно специалистов с таким айди")


@router.callback_query(F.data == "trustedpartners")
async def cmd_trustedpartners(callback: CallbackQuery):
    print(callback.from_user.id)
    await callback.message.edit_text(text.text_question, reply_markup=kb.trusted_partners, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "cooperation")
async def cmd_cooperation(callback: CallbackQuery):
    await callback.message.edit_text(text.text_cooperation, reply_markup=kb.trusted_partners, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "registration in the chat")
async def cmd_registration(callback: CallbackQuery):
    await callback.message.edit_text(text.reg_stage1, reply_markup=kb.registration, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "Startuser")
async def cmd_startuser(callback: CallbackQuery, state: FSMContext):
    currentCity.clear()
    await state.clear()
    await callback.message.edit_text("Выберите раздел 👇", reply_markup=kb.startuser_kb)
    await callback.answer()


@router.callback_query(F.data == "Startprofi")
async def cmd_startuser(callback: CallbackQuery, state: FSMContext):
    currentCity.clear()
    await state.clear()
    await callback.message.edit_text("Выберите раздел 👇", reply_markup=kb.startprofi_kb)
    await callback.answer()


@router.callback_query(F.data == "go1")
async def cmd_go1(callback: CallbackQuery):
    await callback.message.edit_text("Вы специалист?", reply_markup=kb.go1, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "nospecialist")
async def cmd_nospecialist(callback: CallbackQuery):
    await callback.message.edit_text(text.text_nospecialist, reply_markup=kb.no_specialist, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "go2")
async def cmd_go2(callback: CallbackQuery):
    await callback.message.edit_text(text.reg_stage2, reply_markup=kb.go2, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "go3")
async def cmd_go3(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("➡️ Напишите своё имя и фамилию (именно в таком порядке)", reply_markup=None)
    await state.set_state(Form.get_fullname)
    await callback.answer()


@router.message(Form.get_fullname)
async def cmd_go4(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await state.set_state(Form.get_city)
    print(1)
    await message.answer("➡️ Город вашего проживания")


@router.message(Form.get_city)
async def cmd_go5(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text.chat_city_text, reply_markup=kb.city_keyboard, parse_mode="HTML")
    await state.set_state(None)


@router.callback_query(CityCheck())
async def cmd_chat_city(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    msg = f"{text.chat_city_text}\n Вы выбрали:\n"
    for i in range(len(currentCity)):
        if currentCity[i] in cf.city_rus:
            msg += f"{i + 1}. {cf.city_rus[currentCity[i]]}\n"
        else:
            msg += f"{i + 1}. {currentCity[i]}\n"
    print(msg)
    await callback.message.edit_text(f'{msg}\nЧтобы закончить выбор городов, нажмите "Завершить"',
                                     reply_markup=kb.city_keyboard2)


@router.callback_query(F.data == "city_add")
async def cmd_add_city(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text.text_no_city)
    await state.set_state(Form.no_city)
    await callback.answer()


@router.callback_query(F.data == "search")
async def cmd_all_search(callback: CallbackQuery):
    await callback.message.edit_text(text.text_find_a_specialist, reply_markup=kb.find_specialist)
    await callback.answer()


@router.callback_query(F.data == "all chat")
async def cmd_all_chat(callback: CallbackQuery):
    await callback.message.edit_text(text.all_chat_text, reply_markup=await kb.all_chat_kb(callback.from_user.id))
    await callback.answer()


@router.callback_query(F.data == "individual selection")
async def cmd_individual_selection(callback: CallbackQuery):
    await callback.message.edit_text(text.select, reply_markup=kb.trusted_partners)
    await callback.answer()


@router.message(Form.no_city)
async def cmd_no_city(message: Message, state: FSMContext, bot: Bot):
    currentCity.append(message.text)
    await message.answer("🤖Я предложу меннеджеру добавить ваш город в список")
    await bot.send_message(cf.ADMIN_ID, f"пользователь @{message.from_user.username} предложил добавить чат города"
                                        f"-> <b>{currentCity[-1]}</b>", parse_mode="HTML")
    msg = f"{text.chat_city_text}\n Вы выбрали:\n"
    for i in range(len(currentCity)):
        if currentCity[i] in cf.city_rus:
            msg += f"{i + 1}. {cf.city_rus[currentCity[i]]}\n"
        else:
            msg += f"{i + 1}. {currentCity[i]}\n"
    print(msg)
    await message.answer(f'{msg}\nЧтобы закончить выбор городов, нажмите "Завершить"',
                         reply_markup=kb.city_keyboard2)
    await state.set_state(None)


@router.callback_query(F.data == "go5")
async def cmd_go6(callback: CallbackQuery):
    await callback.message.edit_text("➡️ Какой основной род услуги вы предоставляете?",
                                     reply_markup=kb.self_cat_keyboard, parse_mode="HTML")
    await callback.answer()


@router.callback_query(CatCheck())
async def cmd_chat_city(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(self_cat=callback.data)
    await callback.message.edit_text("➡️Какая ваша специализация?", reply_markup=kb.self_subcat_keyboard)


@router.callback_query(F.data == "look")
async def cmd_look(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    res = await request.seach_profi(user_id)
    count = 0
    msg = f"➡️ Ознакомиться с правилами чата - согласие\nИмя Фамилия: <b>{res[0][3]}</b>\nГород: <b>{res[0][4]}</b>\nТелефон: <b>{res[0][8]}</b>\n"
    for i in res:
        count += 1
        msg += f"<b>{count}.</b>\n"
        text = f"Чат города: {i[5]}\n  Категория: {i[6]}\n  Подкатегория: {i[7]}\n  Ссылка на промо: {i[9]}\n  Стоимость услуг: {i[10]}\n"
        msg += text
    await callback.message.edit_text(msg, reply_markup=kb.update_data_kb, parse_mode="HTML")


@router.callback_query(SubCatCheck())
async def cmd_phone(callback: CallbackQuery, state: FSMContext):
    await state.update_data(self_subcat=callback.data)
    await callback.message.edit_text("➡️ Ваш контактный номер", reply_markup=None)
    await callback.answer()
    await state.set_state(Form.phone)


@router.callback_query(F.data == "update")
async def cmd_update(callback: CallbackQuery):
    await callback.message.edit_text("🤖Что желаете изменить?", reply_markup=kb.update_data_kb2)
    await callback.answer()


@router.callback_query(F.data == "updatefullname")
async def cmd_updatefullname(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите новое имя и фамилии(обязательно в таком порядке)")
    await state.set_state(Update.get_fullname)
    await callback.answer()


@router.message(Update.get_fullname)
async def newfullname(message: Message, bot: Bot):
    new = message.text
    user_id = message.from_user.id
    await request.update_profi_fullname(new, user_id)
    await bot.send_message(cf.ADMIN_ID, f"Специалист с айди = <b>{user_id}</b> поменял Имя и Фамилию на {new}", parse_mode="HTML")
    await message.answer("🤖Имя и Фамилия изменины успешно",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                           [[InlineKeyboardButton(text="Меню",
                                                                                  callback_data="Startprofi")]]))


@router.callback_query(F.data == "updatecity")
async def cmd_updatecity(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите новое название вашего города")
    await state.set_state(Update.get_city)
    await callback.answer()


@router.message(Update.get_city)
async def newcity(message: Message, bot: Bot):
    new = message.text
    user_id = message.from_user.id
    await request.update_profi_city(new, user_id)
    await bot.send_message(cf.ADMIN_ID, f"Специалист с айди = <b>{user_id}</b> поменял город на {new}", parse_mode="HTML")
    await message.answer("🤖Имя города изменино успешно",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                           [[InlineKeyboardButton(text="Меню",
                                                                                  callback_data="Startprofi")]]))


@router.callback_query(F.data == "updatephone")
async def cmd_updatephone(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите новый номер телефона")
    await state.set_state(Update.get_phone)
    await callback.answer()


@router.message(Update.get_phone)
async def newphone(message: Message, bot: Bot):
    new = message.text
    user_id = message.from_user.id
    await request.update_profi_phone(new, user_id)
    await bot.send_message(cf.ADMIN_ID, f"Специалист с айди = <b>{user_id}</b> поменял номер телефона на {new}", parse_mode="HTML")
    await message.answer("🤖Номер телефона изменен успешно",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                           [[InlineKeyboardButton(text="Меню",
                                                                                  callback_data="Startprofi")]]))


@router.callback_query(F.data == "pro search")
async def cmd_pro_search(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("В каком городе вы ищете специалиста?", reply_markup=kb.city_keyboard3)
    await callback.answer()


@router.callback_query(CityChecksearch())
async def cmd_city_search(callback: CallbackQuery, state: FSMContext):
    res = cf.city_rus[callback.data[0:-1]]
    print(res)
    await state.update_data(city_search=res)
    await callback.message.edit_text("Профессионала какого рода услуг вы ищете?", reply_markup=kb.self_cat_keyboard2)


@router.callback_query(CatChecksearch())
async def cmd_selfcat_search(callback: CallbackQuery, state: FSMContext):
    print(callback.data[0:-1])
    res = cf.self_cat2[callback.data]
    await state.update_data(self_cat_search=res)
    await callback.message.edit_text("Выберите категорию:", reply_markup=kb.self_subcat_keyboard2)


@router.callback_query(SubCatChecksearch())
async def cmd_selfsubcat_search(callback: CallbackQuery, state: FSMContext):
    res = cf.self_subcat2[callback.data]
    await state.update_data(self_subcat_search=res)
    data = await state.get_data()
    sets = set()
    try:
        res = await request.seach_Pro(data["city_search"], data["self_cat_search"], data["self_subcat_search"])
        for i in range(5):
            sets.add(random.choice(res))
        msg = "Вы можете связаться со следующими специалистами:\n"
        count = 0
        for i in sets:
            count += 1
            msg += f"{count}. {i[1]}: {i[0]}"
            print(msg)
        await callback.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                                [[InlineKeyboardButton(text="Найти еще",
                                                                                                       callback_data="repead")]]))
    except Exception:
        await callback.message.edit_text("🤖По вашему запросу никого не нашлось",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                           [[InlineKeyboardButton(text="Меню",
                                                                                                  callback_data="Startprofi")]]))


@router.callback_query(F.data == "repead")
async def cmd_repead(callback: CallbackQuery, state: FSMContext, bot: Bot, count_click: int):
    data = await state.get_data()
    sets = set()
    if count_click > 2:
        await bot.send_message(cf.ADMIN_ID, f"Пользователь с айди = {callback.from_user.id} нажал на кнопку 'Найти еще'"
                                            f"больше 2 раз")
    try:
        res = await request.seach_Pro(data["city_search"], data["self_cat_search"], data["self_sub_cat_search"])
        for i in range(5):
            sets.add(random.choice(res))
        msg = "Вы можете связаться со следующими специалистами:\n"
        count = 0
        for i in sets:
            count += 1
            msg += f"{count}. {i[1]}: {i[0]}"
            print(msg)
        await callback.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                                [[InlineKeyboardButton(text="Найти еще",
                                                                                                       callback_data="repead")]]))
    except Exception:
        await callback.message.edit_text("🤖По вашему запросу никого не нашлось",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                           [[InlineKeyboardButton(text="Меню",
                                                                                                  callback_data="Startprofi")]]))


@router.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("💸 Укажите примерную стоимость услуг (так же укажите валюту)")
    await state.set_state(Form.price)


@router.message(Form.price)
async def price_cmd(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text.promo_link_text, reply_markup=kb.promo_link)


@router.callback_query(F.data == "link")
async def cmd_link(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.promo_link)
    await callback.message.edit_text("Оставить здесь👇")
    await callback.answer()


@router.callback_query(F.data == "pass")
async def cmd_pass(callback: CallbackQuery, state: FSMContext):
    await state.update_data(promo_link="")
    await callback.message.edit_text(text.chat_rules, reply_markup=kb.chat_rules)
    await callback.answer()


@router.message(Form.promo_link)
async def promo_link_cmd(message: Message, state: FSMContext):
    await state.update_data(promo_link=message.text)
    await message.answer(text.chat_rules, reply_markup=kb.chat_rules)


@router.callback_query(F.data == "chat rules")
async def cmd_chat_rules(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        full_name = data["fullname"]
        city = data["city"]
        chat_city = ", ".join([cf.city_rus[i] for i in currentCity if i in cf.city_rus])
        phone = data["phone"]
        self_cat = cf.self_cat[data["self_cat"]]
        self_subcat = cf.self_subcat[data["self_subcat"]]
        promo_link = data["promo_link"]
        price = data["price"]
        await callback.message.edit_text(
            text.set_chat_rules(full_name, city, chat_city, phone, self_cat, self_subcat, promo_link, price),
            reply_markup=kb.open_rules)
    except Exception as ex:
        print(ex)
        await callback.message.edit_text(
            "🤖Произошла ошибка. Какие-то данные не сохранились повтарите попытку пожалуйста")
    await callback.answer()


@router.callback_query(F.data == "read and agree")
async def cmd_read_and_agree(callback: CallbackQuery, state: FSMContext, bot: Bot):
    try:
        data = await state.get_data()
        full_name = data["fullname"]
        city = data["city"]
        chat_city = [cf.city_rus[i] for i in currentCity if i in cf.city_rus]
        phone = data["phone"]
        self_cat = cf.self_cat[data["self_cat"]]
        self_subcat = cf.self_subcat[data["self_subcat"]]
        promo_link = data["promo_link"]
        price = data["price"]
        user_name = callback.from_user.username
        user_id = callback.from_user.id
        for item in chat_city:
            await request.add_profi(user_name, user_id, full_name, city, item, phone, self_cat, self_subcat, promo_link,
                                    price)
            await bot.send_message(cf.ADMIN_ID,
                                   f"Зарегистрировался новый специалист - @{callback.from_user.username} "
                                   f"-> <b>{full_name}</b>", parse_mode="HTML")
        await callback.message.edit_text(text.text_add_base, reply_markup=await kb.add_base_kb(user_id))
    except Exception:
        await callback.message.edit_text(
            "🤖Произошла ошибка. Какие-то данные не сохранились повтарите попытку пожалуйста")
        await callback.answer()


@router.callback_query(F.data == "subscription")
async def cmd_subscription(callback: CallbackQuery):
    await callback.message.edit_text(text.info_subscribe, reply_markup=kb.subscribe_info, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data.startswith("Evento"))
async def cmd_dont_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(text.no_subscribe, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Меню",
                                               callback_data="Startprofi")]]))
    await callback.answer()


@router.callback_query(F.data == "advertisement")
async def cmd_advertisement(callback: CallbackQuery):
    await callback.message.edit_text("Объявление кому?", parse_mode="HTML", reply_markup=kb.admin_panel2)
    await callback.answer()


@router.callback_query(F.data == "all advertisement")
async def advertisement2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ADMIN.advertisement)
    await callback.message.edit_text("🤖Напишите текст объявления")


@router.message(ADMIN.advertisement)
async def alladvertisement(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    msg = message.text
    await state.clear()
    if "user_id" in data:
        try:
            await bot.send_message(data["user_id"], f"{msg}\n ⚫️Объявление Администрации Бота⚫️")
            await message.answer("Объявления отправлены")
        except Exception:
            await message.answer("Произошла ошибка")
    else:
        try:
            idies = await request.seach_user_all()
            for i in idies:
                await bot.send_message(i[0], f"{msg}\n ⚫️Объявление Администрации Бота⚫️")
            await message.answer("Объявления отправлены")
        except Exception:
            await message.answer("Произошла ошибка")


@router.callback_query(F.data == "user advertisement")
async def advertisement3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ADMIN.user_id)
    await callback.message.edit_text("🤖напишите айди получателя")


@router.message(ADMIN.user_id)
async def useradvertisement(message: Message, state: FSMContext):
    await state.update_data(user_id=message.text)
    await state.set_state(ADMIN.advertisement)
    await message.answer("🤖Напишите текст объявления")


@router.callback_query(F.data == "updatebase")
async def update_base_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    res = await request.seach_profi(user_id)
    count = 0
    ids = []
    msg = f"Записи в базе спецов:\n "
    for i in res:
        ids.append(i[0])
        count += 1
        msg += f"<b>{count}.</b>\n"
        text = f"Чат города: {i[5]}\n  Категория: {i[6]}\n  Подкатегория: {i[7]}\n  Ссылка на промо: {i[9]}\n  Стоимость услуг: {i[10]}\n"
        msg += text
    msg += "<b>Выберите одну из записей в нашей базе. Для этого введите номер из списка 👆</b>"
    await callback.message.edit_text(msg, parse_mode="HTML")
    await state.set_state(UpdateBase.get_id)


@router.message(UpdateBase.get_id)
async def update_base_get_id(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        res = await request.seach_profi(user_id)
        count = 0
        ids = []
        for i in res:
            ids.append(i[0])
            count += 1
        data = int(message.text)
        if 1 <= data <= len(ids):
            await message.answer("Что желаете изменить?", reply_markup=kb.update_base)
            await state.update_data(id=data)
        else:
            raise Exception
    except Exception:
        await message.answer("Вы ввели неверный номер из списка. Попробуйте еще раз")


@router.callback_query(F.data == "update_promo_link")
async def update_base_promo_link(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите новую ссылку на промо материалы")
    await state.set_state(UpdateBase.get_promo_link)


@router.message(UpdateBase.get_promo_link)
async def update_get_base_promo_link(message: Message, state: FSMContext, bot: Bot):
    data = message.text
    id = (await state.update_data())["id"]
    await request.update_profi_promo_link(data, id)
    await bot.send_message(cf.ADMIN_ID,
                           f"Специалист с айди = <b>{message.from_user.id}</b> поменял цену ссылку на промо с айди {id} на {data}",
                           parse_mode="HTML")
    await message.answer("Данные успешно изменены")


@router.callback_query(F.data == "update_price")
async def update_base_price(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите новую цену")
    await state.set_state(UpdateBase.get_price)


@router.message(UpdateBase.get_price)
async def update_get_base_price(message: Message, state: FSMContext, bot: Bot):
    data = message.text
    id = (await state.update_data())["id"]
    await request.update_profi_price(data, id)
    await bot.send_message(cf.ADMIN_ID, f"Специалист с айди = <b>{message.from_user.id}</b> поменял цену за свои услуги с айди {id} на {data}",
                           parse_mode="HTML")
    await message.answer("Данные успешно изменены")

@router.callback_query(F.data == "question")
async def update_base_price(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Задайте ваш вопрос")
    await state.set_state(Question.get_question)


@router.message(Question.get_question)
async def update_get_base_price(message: Message, state: FSMContext, bot: Bot):
    data = message.text
    await bot.send_message(cf.ADMIN_ID, f"<b>Пользователь с айди = {message.from_user.id} задал вопрос</b>:\n{data}", parse_mode="HTML")
    await message.answer("Вопрос отправлен успешно")


@router.message(F.text.lower() == "тестреф")
async def test_ref(message: Message):
    await message.answer(text.testref)
