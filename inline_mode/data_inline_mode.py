from faker import Faker
from random import randint, choice


fake = Faker("ru_RU")
fake_en = Faker()


GENERATE_DATA = {
    "День месяца": {
        "description": f"Пример: {fake.day_of_month()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/sun_2600-fe0f.png",
    },
    "День недели": {
        "description": f"Пример: {fake.day_of_week()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/newspaper_1f4f0.png",
    },
    "Номер месяца": {
        "description": f"Пример: {fake.month()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/spiral-calendar_1f5d3-fe0f.png",
    },
    "Название месяца": {
        "description": f"Пример: {fake.month_name()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/calendar_1f4c5.png",
    },
    "Год": {
        "description": f"Пример: {fake.year()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/globe-showing-asia-australia_1f30f.png",
    },
    "Век": {
        "description": f"Пример: {fake.century()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/funeral-urn_26b1-fe0f.png",
    },
    "Дата рождения": {
        "description": f"Пример: {fake.date_of_birth().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/baby_1f476.png",
    },
    "Случайная дата": {
        "description": f"Пример: {fake.date_time_ad().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/spiral-notepad_1f5d2-fe0f.png",
    },
    "Дата в этом месяце": {
        "description": f"Пример: {fake.date_this_month().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/calendar_1f4c5.png",
    },
    "Дата в этом году": {
        "description": f"Пример: {fake.date_this_year().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/globe-showing-europe-africa_1f30d.png",
    },
    "Дата в этом десятилетии": {
        "description": f"Пример: {fake.date_this_decade().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/dizzy_1f4ab.png",
    },
    "Дата в этом веке": {
        "description": f"Пример: {fake.date_this_century().strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/amphora_1f3fa.png",
    },
    "Будущая дата": {
        "description": f"Пример: {fake.future_date(end_date='+100y').strftime('%d.%m.%Y')}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/crystal-ball_1f52e.png",
    },
    "Время": {
        "description": f"Пример: {fake.time()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/four-oclock_1f553.png",
    },
    "Часовые зоны": {
        "description": f"Пример: {fake.timezone()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/airplane_2708-fe0f.png",
    },
    "Адрес": {
        "description": f"Пример: {fake.address()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/placard_1faa7.png",
    },
    "Номер дома": {
        "description": f"Пример: {fake.building_number()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/house_1f3e0.png",
    },
    "Адрес улицы": {
        "description": f"Пример: {fake.street_address()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/houses_1f3d8-fe0f.png",
    },
    "Название улицы": {
        "description": f"Пример: {fake.street_name()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/railway-track_1f6e4-fe0f.png",
    },
    "Город": {
        "description": f"Пример: {fake.city()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/cityscape_1f3d9-fe0f.png",
    },
    "Субъекты РФ": {
        "description": f"Пример: {fake.administrative_unit()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/flag-russia_1f1f7-1f1fa.png",
    },
    "Почтовый индекс": {
        "description": f"Пример: {fake.postcode()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/open-mailbox-with-raised-flag_1f4ec.png",
    },
    "Долгота": {
        "description": f"Пример (от -180 до 180): {fake.longitude()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/left-right-arrow_2194-fe0f.png",
    },
    "Широта": {
        "description": f"Пример (от -90 до 90): {fake.latitude()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/up-down-arrow_2195-fe0f.png",
    },
    "Случайные координаты": {
        "description": f"Пример (шир., долг.): {', '.join([str(float(i)) for i in fake.latlng()])}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/control-knobs_1f39b-fe0f.png",
    },
    "Страна": {
        "description": f"Пример: {fake.country()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/flag-united-nations_1f1fa-1f1f3.png",
    },
    "Случайная точка России": {
        "description": "Пример: Случайная геопозиция в России",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/flag-russia_1f1f7-1f1fa.png",
    },
    "Случайная точка в мире": {
        "description": "Пример: Случайная геопозиция в мире",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/globe-showing-americas_1f30e.png",
    },
    "Случайная буква": {
        "description": f'Пример (строчная, заглавная): {choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/b-button-blood-type_1f171-fe0f.png",
    },
    "Строчная буква": {
        "description": f'Пример: {choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/input-latin-lowercase_1f521.png",
    },
    "Заглавная буква": {
        "description": f'Пример: {choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/input-latin-uppercase_1f520.png",
    },
    "Случайные буквы": {
        "description": f'Пример (до 20): {" ".join(choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") for _ in range(randint(5, 20)))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/ab-button-blood-type_1f18e.png",
    },
    "Случайное слово": {
        "description": f'Пример (всего 500): {fake.word()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/new-button_1f195.png",
    },
    "Случайные слова": {
        "description": f'Пример (до 10): {" ".join(fake.words(nb=randint(2, 10)))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/free-button_1f193.png",
    },
    "Параграф": {
        "description": f'Пример (до 8 предложений): {fake.paragraph(nb_sentences=randint(1, 8))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/memo_1f4dd.png",
    },
    "Предложение": {
        "description": f'Пример (до 15 слов): {fake.sentence(nb_words=randint(3, 15))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/page-facing-up_1f4c4.png",
    },
    "Предложения": {
        "description": f'Пример (до 5): {" ".join(fake.sentences(nb=randint(2, 5)))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/bookmark-tabs_1f4d1.png",
    },
    "Текст": {
        "description": f'Пример (до 1000 символов): {fake.text(max_nb_chars=1000)}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/open-book_1f4d6.png",
    },
    "Номерной знак": {
        "description": f'Пример (включая специальные номера): {fake.license_plate()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/bus-stop_1f68f.png",
    },
    "ВИН-номер": {
        "description": f'Пример (идентификатор): {fake.vin()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/taxi_1f695.png",
    },
    "Банковская карта": {
        "description": f'Пример: {fake.credit_card_full()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/credit-card_1f4b3.png",
    },
    "Платёжная система": {
        "description": f'Пример: {fake.credit_card_provider()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/money-bag_1f4b0.png",
    },
    "Банк": {
        "description": f'Пример: {fake.bank()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/bank_1f3e6.png",
    },
    "Номер карты": {
        "description": f'Пример: {fake.credit_card_number()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/input-numbers_1f522.png",
    },
    "Дата карты": {
        "description": f'Пример: {fake.credit_card_expire()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/spiral-calendar_1f5d3-fe0f.png",
    },
    "Код безопасности": {
        "description": f'Пример (код на заднем обороте карты): {fake.credit_card_security_code()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/shushing-face_1f92b.png",
    },
    "Название маленькой компании": {
        "description": f'Пример: {fake.company()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/newspaper_1f4f0.png",
    },
    "Название крупной компании": {
        "description": f'Пример: {fake.large_company()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/office-building_1f3e2.png",
    },
    "Слоган компании": {
        "description": f'Пример: {fake.catch_phrase()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/money-with-wings_1f4b8.png",
    },
    "Деятельность компании": {
        "description": f'Пример: {fake.bs()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/toolbox_1f9f0.png",
    },
    "ИНН": {
        "description": f'Пример (Идентификационный номер налогоплательщика): {fake.businesses_inn()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/ticket_1f3ab.png",
    },
    "ОГРН": {
        "description": f'Пример (Основной государственный регистрационный номер): {fake.businesses_ogrn()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/scroll_1f4dc.png",
    },
    "Валюта": {
        "description": f'Пример: {"{0} ({1})".format(*[i for i in fake.currency()])}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/dollar-banknote_1f4b5.png",
    },
    "Название валюты": {
        "description": f'Пример: {fake.currency_name()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/coin_1fa99.png",
    },
    "Код валюты": {
        "description": f'Пример: {fake.currency_code()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/pager_1f4df.png",
    },
    "Символ валюты": {
        "description": f'Пример: {fake.currency_symbol()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/diamond-with-a-dot_1f4a0.png",
    },
    "Кол-во денег": {
        "description": f'Пример: {fake.pricetag()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/antenna-bars_1f4f6.png",
    },
    "Криптовалюта": {
        "description": f'Пример: {"{0} ({1})".format(*[i for i in fake.cryptocurrency()])}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/optical-disk_1f4bf.png",
    },
    "Название криптовалюты": {
        "description": f'Пример: {fake.cryptocurrency_name()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/gear_2699-fe0f.png",
    },
    "Код криптовалюты": {
        "description": f'Пример: {fake.cryptocurrency_code()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/dvd_1f4c0.png",
    },
    "Профессия": {
        "description": f"Пример: {fake.job()}",
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/hammer-and-wrench_1f6e0-fe0f.png",
    },
    "Название цвета": {
        "description": f'Пример: {fake.color_name()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/rainbow_1f308.png",
    },
    "Цвет палитры HEX": {
        "description": f'Пример (#FFFFFF): {fake.hex_color()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/alien-monster_1f47e.png",
    },
    "Цвет палитры RGB": {
        "description": f'Пример (256,256,256): {fake.rgb_color()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/small-blue-diamond_1f539.png",
    },
    "Цвет палитры CSS RGB": {
        "description": f'Пример (rgb(256,256,256)): {fake.rgb_css_color()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/large-orange-diamond_1f536.png",
    },
    "Эмодзи": {
        "description": f'Пример: {fake.emoji()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/performing-arts_1f3ad.png",
    },
    "Мужское Ф.И.О.": {
        "description": f'Пример: {fake.name_male()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/mens-room_1f6b9.png",
    },
    "Мужское имя": {
        "description": f'Пример: {fake.first_name_male()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/identification-card_1faaa.png",
    },
    "Мужская фамилия": {
        "description": f'Пример: {fake.last_name_male()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/family-man-woman-girl-boy_1f468-200d-1f469-200d-1f467-200d-1f466.png",
    },
    "Мужское отчество": {
        "description": f'Пример: {fake.middle_name_male()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/man-blond-hair_1f471-200d-2642-fe0f.png",
    },
    "Женское Ф.И.О.": {
        "description": f'Пример: {fake.name_female()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/womens-room_1f6ba.png",
    },
    "Женское имя": {
        "description": f'Пример: {fake.first_name_female()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/identification-card_1faaa.png",
    },
    "Женская фамилия": {
        "description": f'Пример: {fake.last_name_female()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/family-man-woman-girl-boy_1f468-200d-1f469-200d-1f467-200d-1f466.png",
    },
    "Женское отчество": {
        "description": f'Пример: {fake.middle_name_female()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/man-blond-hair_1f471-200d-2642-fe0f.png",
    },
    "Язык": {
        "description": f'Пример: {fake.language_name()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/tongue_1f445.png",
    },
    "Код языка": {
        "description": f'Пример: {fake.language_code().upper()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/keyboard_2328-fe0f.png",
    },
    "Код страны": {
        "description": f'Пример: {fake.country_calling_code()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/triangular-flag_1f6a9.png",
    },
    "MSISDN": {
        "description": f'Пример: {fake.msisdn()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/television_1f4fa.png",
    },
    "Номер телефона": {
        "description": f'Пример: {fake.phone_number()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/telephone-receiver_1f4de.png",
    },
    "Профиль": {
        "description": "Пример: Имя: {name}\nПочта: {mail}".format(**fake.profile()),
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/man-blond-hair_1f471-200d-2642-fe0f.png",
    },
    "Упрощённый профиль": {
        "description": "Пример: Имя: {name}\nПочта: {mail}".format(**fake.simple_profile()),
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/baby_1f476.png",
    },
    "Личный email": {
        "description": f'Пример: {fake.free_email()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/envelope_2709-fe0f.png",
    },
    "Email для бизнеса": {
        "description": f'Пример: {fake.company_email()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/incoming-envelope_1f4e8.png",
    },
    "Файл": {
        "description": f'Пример: {fake_en.file_name()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/file-folder_1f4c1.png",
    },
    "Расширение файла": {
        "description": f'Пример: {fake_en.file_extension()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/link_1f517.png",
    },
    "Путь к файлу": {
        "description": f'Пример: {fake_en.file_path(depth=randint(1, 5))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/card-index-dividers_1f5c2-fe0f.png",
    },
    "Имя домена": {
        "description": f'Пример: {fake.domain_name(levels=randint(1, 3))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/printer_1f5a8-fe0f.png",
    },
    "Случайное URL": {
        "description": f'Пример: {fake.url()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/globe-with-meridians_1f310.png",
    },
    "Имя хостинга": {
        "description": f'Пример: {fake.hostname(levels=randint(1, 3))}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/file-cabinet_1f5c4-fe0f.png",
    },
    "Публичный IPv4": {
        "description": f'Пример: {fake.ipv4_public()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/unlocked_1f513.png",
    },
    "Приватный IPv4": {
        "description": f'Пример: {fake.ipv4_private()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/locked-with-key_1f510.png",
    },
    "IPv6": {
        "description": f'Пример: {fake.ipv6()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/locked-with-pen_1f50f.png",
    },
    "MAC-адрес": {
        "description": f'Пример: {fake.mac_address()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/electric-plug_1f50c.png",
    },
    "Токен Android": {
        "description": f'Пример: {fake.android_platform_token()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/t-rex_1f996.png",
    },
    "Токен IOS": {
        "description": f'Пример: {fake.ios_platform_token()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/green-apple_1f34f.png",
    },
    "Токен Windows": {
        "description": f'Пример: {fake.windows_platform_token()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/night-with-stars_1f303.png",
    },
    "Токен Linux": {
        "description": f'Пример: {fake.linux_platform_token()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/penguin_1f427.png",
    },
    "Токен MacOS": {
        "description": f'Пример: {fake.mac_platform_token()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/desktop-computer_1f5a5-fe0f.png",
    },
    "User-Agent": {
        "description": f'Пример: {fake.user_agent()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/smiling-face-with-sunglasses_1f60e.png",
    },
    "User-Agent (Chrome)": {
        "description": f'Пример: {fake.chrome()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/dna_1f9ec.png",
    },
    "User-Agent (Safari)": {
        "description": f'Пример: {fake.safari()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/compass_1f9ed.png",
    },
    "User-Agent (Firefox)": {
        "description": f'Пример: {fake.firefox()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/fox_1f98a.png",
    },
    "User-Agent (Opera)": {
        "description": f'Пример: {fake.opera()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/ring-buoy_1f6df.png",
    },
    "User-Agent (Internet Explorer)": {
        "description": f'Пример: {fake.internet_explorer()}',
        "thumbnail_url": "https://em-content.zobj.net/source/apple/354/spider-web_1f578-fe0f.png",
    },
    # "": {
    #     "description": f'Пример: {}',
    #     "thumbnail_url": "",
    # },
}


def fake_genarate_data(name_data: str):
    return {
        "День месяца": fake.day_of_month(),
        "День недели": fake.day_of_week(),
        "Номер месяца": fake.month(),
        "Название месяца": fake.month_name(),
        "Год": fake.year(),
        "Век": fake.century(),
        "Дата рождения": fake.date_of_birth().strftime('%d.%m.%Y'),
        "Случайная дата": fake.date_time_ad().strftime('%d.%m.%Y'),
        "Дата в этом месяце": fake.date_this_month().strftime('%d.%m.%Y'),
        "Дата в этом году": fake.date_this_year().strftime('%d.%m.%Y'),
        "Дата в этом десятилетии": fake.date_this_decade().strftime('%d.%m.%Y'),
        "Дата в этом веке": fake.date_this_century().strftime('%d.%m.%Y'),
        "Будущая дата": fake.future_date(end_date='+100y').strftime('%d.%m.%Y'),
        "Время": fake.time(),
        "Часовые зоны": fake.timezone(),
        "Адрес": fake.address(),
        "Номер дома": fake.building_number(),
        "Адрес улицы": fake.street_address(),
        "Название улицы": fake.street_name(),
        "Город": fake.city(),
        "Субъекты РФ": fake.administrative_unit(),
        "Почтовый индекс": fake.postcode(),
        "Долгота": fake.longitude(),
        "Широта": fake.latitude(),
        "Случайные координаты": ', '.join([str(float(i)) for i in fake.latlng()]),
        "Страна": fake.country(),
        "Случайная точка России": fake.local_latlng(country_code="RU"),
        "Случайная точка в мире": fake.location_on_land(),
        "Случайная буква": choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
        "Строчная буква": choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
        "Заглавная буква": choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
        "Случайные буквы": " ".join(choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") for _ in range(randint(5, 20))),
        "Случайное слово": fake.word(),
        "Случайные слова": " ".join(fake.words(nb=randint(2, 10))),
        "Параграф": fake.paragraph(nb_sentences=randint(1, 8)),
        "Предложение": fake.sentence(nb_words=randint(3, 15)),
        "Предложения": " ".join(fake.sentences(nb=randint(2, 5))),
        "Текст": fake.text(max_nb_chars=1000),
        "Номерной знак": fake.license_plate(),
        "ВИН-номер": fake.vin(),
        "Банковская карта": fake.credit_card_full(),
        "Платёжная система": fake.credit_card_provider(),
        "Банк": fake.bank(),
        "Номер карты": fake.credit_card_number(),
        "Дата карты": fake.credit_card_expire(),
        "Код безопасности": fake.credit_card_security_code(),
        "Название маленькой компании": fake.company(),
        "Название крупной компании": fake.large_company(),
        "Слоган компании": fake.catch_phrase(),
        "Деятельность компании": fake.bs(),
        "ИНН": fake.businesses_inn(),
        "ОГРН": fake.businesses_ogrn(),
        "Валюта": "{0} ({1})".format(*[i for i in fake.currency()]),
        "Название валюты": fake.currency_name(),
        "Код валюты": fake.currency_code(),
        "Символ валюты": fake.currency_symbol(),
        "Кол-во денег": fake.pricetag(),
        "Криптовалюта": "{0} ({1})".format(*[i for i in fake.cryptocurrency()]),
        "Название криптовалюты": fake.cryptocurrency_name(),
        "Код криптовалюты": fake.cryptocurrency_code(),
        "Профессия": fake.job(),
        "Название цвета": fake.color_name(),
        "Цвет палитры HEX": fake.hex_color(),
        "Цвет палитры RGB": fake.rgb_color(),
        "Цвет палитры CSS RGB": fake.rgb_css_color(),
        "Эмодзи": fake.emoji(),
        "Мужское Ф.И.О.": fake.name_male(),
        "Мужское имя": fake.first_name_male(),
        "Мужская фамилия": fake.last_name_male(),
        "Мужское отчество": fake.middle_name_male(),
        "Женское Ф.И.О.": fake.name_female(),
        "Женское имя": fake.first_name_female(),
        "Женская фамилия": fake.last_name_female(),
        "Женское отчество": fake.middle_name_female(),
        "Язык": fake.language_name(),
        "Код языка": fake.language_code().upper(),
        "Код страны": fake.country_calling_code(),
        "MSISDN": fake.msisdn(),
        "Номер телефона": fake.phone_number(),
        "Профиль": "<i>Имя:</i> <code>{name}</code>\n<i>Почта:</i> <code>{mail}</code>" \
            "\n<i>Никнейм:</i> <code>{username}</code>\n<i>Дата рождения:</i> <code>{birthdate}</code>" \
            "\n<i>Адрес:</i> <code>{address}</code>\n<i>Группа крови:</i> <code>{blood_group}</code>" \
            "\n<i>Профессия:</i> <code>{job}</code>\n<i>Компания:</i> <code>{company}</code>".format(**fake.profile()),
        "Упрощённый профиль": "<i>Имя:</i> <code>{name}</code>\n<i>Почта:</i> <code>{mail}</code>" \
            "\n<i>Никнейм:</i> <code>{username}</code>\n<i>Дата рождения:</i> <code>{birthdate}</code>" \
            "\n<i>Адрес:</i> <code>{address}</code>".format(**fake.simple_profile()),
        "Личный email": fake.free_email(),
        "Email для бизнеса": fake.company_email(),
        "Файл": fake_en.file_name(),
        "Расширение файла": fake_en.file_extension(),
        "Путь к файлу": fake_en.file_path(depth=randint(1, 5)),
        "Имя домена": fake.domain_name(levels=randint(1, 3)),
        "Случайное URL": fake.url(),
        "Имя хостинга": fake.hostname(levels=randint(1, 3)),
        "Публичный IPv4": fake.ipv4_public(),
        "Приватный IPv4": fake.ipv4_private(),
        "IPv6": fake.ipv6(),
        "MAC-адрес": fake.mac_address(),
        "Токен Android": fake.android_platform_token(),
        "Токен IOS": fake.ios_platform_token(),
        "Токен Windows": fake.windows_platform_token(),
        "Токен Linux": fake.linux_platform_token(),
        "Токен MacOS": fake.mac_platform_token(),
        "User-Agent": fake.user_agent(),
        "User-Agent (Chrome)": fake.chrome(),
        "User-Agent (Safari)": fake.safari(),
        "User-Agent (Firefox)": fake.firefox(),
        "User-Agent (Opera)": fake.opera(),
        "User-Agent (Internet Explorer)": fake.internet_explorer(),
    }[name_data]