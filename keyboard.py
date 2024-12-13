from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import config as cf
import request

startuser_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация в чате", callback_data="registration in the chat")],
    [InlineKeyboardButton(text="Подписка", callback_data="subscription"),
     InlineKeyboardButton(text="Pro поиск", callback_data="pro search")],
    [InlineKeyboardButton(text="Задать вопрос", callback_data="question"),
     InlineKeyboardButton(text="Сотрудничество", callback_data="cooperation")],
    [InlineKeyboardButton(text="Проверенные партнеры", callback_data="trustedpartners")]
])

startprofi_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Все чаты", callback_data="all chat"),
     InlineKeyboardButton(text="Посмотреть анкету", callback_data="look")],
    [InlineKeyboardButton(text="Подписка", callback_data="subscription"),
     InlineKeyboardButton(text="Pro поиск", callback_data="pro search")],
    [InlineKeyboardButton(text="Задать вопрос", callback_data="question"),
     InlineKeyboardButton(text="Сотрудничество", callback_data="cooperation")],
    [InlineKeyboardButton(text="Проверенные партнеры", callback_data="trustedpartners")]
])

registration = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Давай", callback_data="go1"),
                                                      InlineKeyboardButton(text="Нет", callback_data="Startuser")]])
go1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="go2"),
                                             InlineKeyboardButton(text="Нет", callback_data="nospecialist")]])
go2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Прочитать оферту", url="https://offer.topeventers.ru/")],
                     [InlineKeyboardButton(text="Да", callback_data="go3"),
                      InlineKeyboardButton(text="Нет", callback_data="Startuser")]])
trusted_partners = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Написать чудесному мессенжеру", url="https://t.me/eventworkadmin")]])

city_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пермь", callback_data='permcity'),
         InlineKeyboardButton(text="Екатеринбург", callback_data='ekbcity'),
         InlineKeyboardButton(text="Тюмень", callback_data='tyumencity'), ],
        [InlineKeyboardButton(text="Челябинск", callback_data='chelyabinskcity'),
         InlineKeyboardButton(text="Ростов-На-Дону", callback_data='rostovcity'), ],
        [InlineKeyboardButton(text="Оренбург", callback_data='orenburgcity'),
         InlineKeyboardButton(text="Новосибирск", callback_data='novosibirskcity'), ],
        [InlineKeyboardButton(text="Нижний Новгород", callback_data='nizhny_novgorodcity'),
         InlineKeyboardButton(text="Самара", callback_data='samaracity'), ],
        [InlineKeyboardButton(text="Казань", callback_data='kazancity'),
         InlineKeyboardButton(text="Краснодар", callback_data='krasnodarcity'),
         InlineKeyboardButton(text="Уфа", callback_data='ufacity'), ],
        [InlineKeyboardButton(text="+Добавить город", callback_data='city_add')]
    ]
)

city_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пермь", callback_data='permcity'),
         InlineKeyboardButton(text="Екатеринбург", callback_data='ekbcity'),
         InlineKeyboardButton(text="Тюмень", callback_data='tyumencity'), ],
        [InlineKeyboardButton(text="Челябинск", callback_data='chelyabinskcity'),
         InlineKeyboardButton(text="Ростов-На-Дону", callback_data='rostovcity'), ],
        [InlineKeyboardButton(text="Оренбург", callback_data='orenburgcity'),
         InlineKeyboardButton(text="Новосибирск", callback_data='novosibirskcity'), ],
        [InlineKeyboardButton(text="Нижний Новгород", callback_data='nizhny_novgorodcity'),
         InlineKeyboardButton(text="Самара", callback_data='samaracity'), ],
        [InlineKeyboardButton(text="Казань", callback_data='kazancity'),
         InlineKeyboardButton(text="Краснодар", callback_data='krasnodarcity'),
         InlineKeyboardButton(text="Уфа", callback_data='ufacity'), ],
        [InlineKeyboardButton(text="+Добавить город", callback_data='city_add')],
        [InlineKeyboardButton(text="Завершить", callback_data="go5")]
    ]
)

no_specialist = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Хочу рассказать о своих услугах", callback_data="cooperation")],
                     [InlineKeyboardButton(text="Хочу найти специалиста", callback_data="search")]])

self_cat_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=cf.self_cat["Organizer"], callback_data="Organizer"),
                      InlineKeyboardButton(text=cf.self_cat["Host"], callback_data="Host")],
                     [InlineKeyboardButton(text=cf.self_cat["Director"], callback_data="Director"),
                      InlineKeyboardButton(text=cf.self_cat["Artist"], callback_data="Artist")],
                     [InlineKeyboardButton(text=cf.self_cat["Content"], callback_data="Content"),
                      InlineKeyboardButton(text=cf.self_cat["Image"], callback_data="Image")],
                     [InlineKeyboardButton(text=cf.self_cat["Decorator"], callback_data="Decorator"),
                      InlineKeyboardButton(text=cf.self_cat["Catering"], callback_data="Catering")],
                     [InlineKeyboardButton(text=cf.self_cat["Technical Equipment"],
                                           callback_data="Technical Equipment"),
                      InlineKeyboardButton(text=cf.self_cat["Others"], callback_data="Others")]]

)


get_phone = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="kk")]])


promo_link = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Оставить ссылку", callback_data="link"), InlineKeyboardButton(text="Пропустить", callback_data="pass")]])

chat_rules = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="➡️ ознакомиться с правилами чата", callback_data="chat rules")]])

open_rules = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="📖Правила чата", url="https://telegra.ph/PRAVILA-CHATA-06-11-37"), InlineKeyboardButton(text="✅ Прочитал и согласен", callback_data="read and agree")]])

find_specialist = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Оформить подписку", callback_data="subscription"), InlineKeyboardButton(text="Индивидуальный подбор", callback_data="individual selection")]])

self_subcat_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Организатор", callback_data="organ"), InlineKeyboardButton(text="Координатор", callback_data="coord")],
                     [InlineKeyboardButton(text="Менеджер", callback_data="menedg")]])


async def all_chat_kb(usid):
    res = await request.seach_profi(usid)
    print(res)
    buttons = []
    for i in res:
        i = i[5]
        button = [InlineKeyboardButton(text=i, url=cf.city_url[i])]
        if button in buttons:
            continue
        buttons.append(button)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def add_base_kb(usid):
    res = set(await request.seach_profi(usid))
    buttons = []
    buttons.append([InlineKeyboardButton(text="⭐️Узнать о подписке", callback_data="subscription")])
    for i in res:
        i = i[5]
        button = [InlineKeyboardButton(text=i, url=cf.city_url[i])]
        if button in buttons:
            continue
        buttons.append(button)
    buttons.append([InlineKeyboardButton(text="Меню", callback_data="Startprofi")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


update_data_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="✏️Изменить данные", callback_data="update")], [InlineKeyboardButton(text="Меню", callback_data="Startprofi")]])

update_data_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Имя Фамилия", callback_data="updatefullname")], [InlineKeyboardButton(text="Город", callback_data="updatecity")],
                     [InlineKeyboardButton(text="Телефон", callback_data="updatephone")], [InlineKeyboardButton(text="Запись в базе спецов", callback_data="updatebase")]])



city_keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пермь", callback_data='permcity1'),
         InlineKeyboardButton(text="Екатеринбург", callback_data='ekbcity1'),
         InlineKeyboardButton(text="Тюмень", callback_data='tyumencity1'), ],
        [InlineKeyboardButton(text="Челябинск", callback_data='chelyabinskcity1'),
         InlineKeyboardButton(text="Ростов-На-Дону", callback_data='rostovcity1'), ],
        [InlineKeyboardButton(text="Оренбург", callback_data='orenburgcity1'),
         InlineKeyboardButton(text="Новосибирск", callback_data='novosibirskcity1'), ],
        [InlineKeyboardButton(text="Нижний Новгород", callback_data='nizhny_novgorodcity1'),
         InlineKeyboardButton(text="Самара", callback_data='samaracity1'), ],
        [InlineKeyboardButton(text="Казань", callback_data='kazancity1'),
         InlineKeyboardButton(text="Краснодар", callback_data='krasnodarcity1'),
         InlineKeyboardButton(text="Уфа", callback_data='ufacity1'), ]
    ]
)

self_cat_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=cf.self_cat2["Organizer1"], callback_data="Organizer1"),
                      InlineKeyboardButton(text=cf.self_cat2["Host1"], callback_data="Host1")],
                     [InlineKeyboardButton(text=cf.self_cat2["Director1"], callback_data="Director1"),
                      InlineKeyboardButton(text=cf.self_cat2["Artist1"], callback_data="Artist1")],
                     [InlineKeyboardButton(text=cf.self_cat2["Content1"], callback_data="Content1"),
                      InlineKeyboardButton(text=cf.self_cat2["Image1"], callback_data="Image1")],
                     [InlineKeyboardButton(text=cf.self_cat2["Decorator1"], callback_data="Decorator1"),
                      InlineKeyboardButton(text=cf.self_cat2["Catering1"], callback_data="Catering1")],
                     [InlineKeyboardButton(text=cf.self_cat2["Technical Equipment1"],
                                           callback_data="Technical Equipment1"),
                      InlineKeyboardButton(text=cf.self_cat2["Others1"], callback_data="Others1")]]

)

self_subcat_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Организатор", callback_data="organ1"), InlineKeyboardButton(text="Координатор", callback_data="coord1")],
                     [InlineKeyboardButton(text="Менеджер", callback_data="menedg1")]])


subscribe_info = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="подключить подписку «Event Life»", callback_data="Evento Life")],
                     [InlineKeyboardButton(text="подключить подписку «Event PRO»", callback_data="Evento Pro")]])

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Поиск специалиста👤", callback_data="search user")],
                     [InlineKeyboardButton(text="Объявление🗣", callback_data="advertisement")]])

admin_panel2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Пользователю👤", callback_data="user advertisement")],
                     [InlineKeyboardButton(text="Всем👥", callback_data="all advertisement")]])