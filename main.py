clean
import subprocess
import sys


def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Устанавливаем {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install_and_import('random')
install_and_import('string')
install_and_import('smtplib')
install_and_import('email')
install_and_import('time')

# Теперь можно использовать библиотеки
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

access_codes = [
    '5555'
]

# Отправители и их пароли
senders = {
    'q7m7gijx695lxwq@rambler.ru': 'gSWkA6GNhFsQ',
    'j04mdloaya53x7@rambler.ru': 'pbg9iTeovOpP',
    '2lrbc8vqibqtdp@rambler.ru': '4pH7rTkdhYQy',
    'oyt0a119a@rambler.ru': 'YtWUskpg9dbe',
    'pm0zdmn3taj@rambler.ru': 'EQaO56vOGT0z',
    '0jg89en4dnft3gy@rambler.ru': 'ORcT6VyuqfOj',
    'jtnkx4nug@rambler.ru': 'QJnCCraZ29W4',
    '46wnffbc5ja9a@rambler.ru': '83ONil4NMNCM',
    'fynnxz186o9nqu@rambler.ru': 'tBUYPxpbtIUZ',
    '82eeqmky1xgs@rambler.ru': 'qBBBGOmjvdXD',
    'hy0d9d8k9l@rambler.ru': 'FoU0nqZ5SyNz',
    'f8dp1nlx1@rambler.ru': 'nPElTNPM6CtN',
    '21zvd1fb8o@rambler.ru': 'HB475wvRSn6u',
    'z10bujl2sqg0s7c@rambler.ru': 'Evc2fb92J4Ht',
    'dn3yskh1qd@rambler.ru': 'WFlGJvZ1NKCr',
    'c9o7mr45h@rambler.ru': 'bxyhrTEmwWBi',
    'zqqjp1kf@rambler.ru': 'mnfUh89FI2yw',
    '4160iirnvmy1@rambler.ru': 'J8reyseIPEvo',
    '653dgodsay1y@rambler.ru': 'z6xvFaLOEEra',
    'fff79boi0m1j@rambler.ru': 'f18n3u4X9OiY',
    'opaal4rbvx3d@rambler.ru': 'wF0ITMAG6IRC',
    'qik4tsmql53g8x@rambler.ru': 'yA7tA5D3eDSw',
    '1k14jmoz@rambler.ru': 'sWNSSbLJnDFq',
    'o5z8eo5sqsw4@rambler.ru': 'KEiGSRU6DVIp',
    '8xstc5d3mw0@rambler.ru': '10K1nkVtnEV2',
    '0a6h12wt7rob5zn@rambler.ru': 'pCuFcHA7OoO7',
    'un3reaf7nyejnj@rambler.ru': 'bNfuxGeD5J27',
    'd5dhqzdexl@rambler.ru': 'wbTuQjz7mLOx',
    'u6j0to97o3wpy5@rambler.ru': 'vdBYCfJTX95b',
    'w6ojpv49vgppy@rambler.ru': 'KMQcVlnMqPqG',
    '8yxjuhil@rambler.ru': 'qYU2onYLChCk',
    'txyx3ig1smtnozm@rambler.ru': 'L6lGjlvlcfkw',
    'bvflo5fz7jbass@rambler.ru': 'cQeLbG5pKjyB',
    '2pv9aa2s@rambler.ru': 'yXorlIH6gJPk',
    'qc1tm1g80mii7a@rambler.ru': 'QOJeBR4Bl539',
    'dups3n4wma@rambler.ru': 'MK0AkIJRuzII',
    'eqskxc4j@rambler.ru': 'Q7nQtfpfV4aC',
    'dtsaczfcn@rambler.ru': 'U7gM6jLd6BCW',
    'osii8g0b7i3naa3@rambler.ru': 'J6GMoNGhzZvN',
    'g60frxkxcv903@rambler.ru': '4oTKimTrbaaL',
    'ahzabsbir@rambler.ru': 'dJiXwmTZpwDS',
    'oqgikk25@rambler.ru': 'fOXrSJrKb0s0',
    'kb22o2o7wk@rambler.ru': 'gKZyLN3ZQ2aK',
    'uroxl44fj@rambler.ru': 'ffzT5bw5ZYfs',
    'hzc0mk4w6oh@rambler.ru': 'SZl201ZGewaQ',
    'lj6y15yofufmr@rambler.ru': '8pPdFTNUJ09E',
    'k1y5oq23@rambler.ru': 'N16WwdpLt0gN',
    'rnlcnngs5de@rambler.ru': 'v5DGPW98uK8Z',
    'pebaizov0tvsi@rambler.ru': 'RplVCXwcQENK',
    'kthyka4amltiae@rambler.ru': 'gBRKLXy2s7Ng',
    'k4dq8kxoc3r@rambler.ru': 'A3bPV7ySWkD8',
    'ow6w5yw9@rambler.ru': 'UL1jGFpnIMXh',
    '337a0wzj0yn0pg@rambler.ru': 'hBUtnylr66gK',
    '6myft801g2j54ru@rambler.ru': '62IZssQd5VEH',
    't5tvpnkp17ffu@rambler.ru': 'h8U7WoT82Zny',
    '9fp6mjzwql6u6@rambler.ru': 'mVd4VLXApv6O',
    'fxg8kjf377eftgz@rambler.ru': 'KfZwRaBGbaPK',
    'punjgqcnzieo2@rambler.ru': 'x2TKLwVzHZt1',
    '48q0s0wvrq0l@rambler.ru': 'GOx1wEJQyPDX',
    '4uwpedmk55@rambler.ru': 'aW35Rdh66ZEa',
    'ck3fu565bg@rambler.ru': 'u3OLuTnAqQar',
    'mq0iwnlzlml7@rambler.ru': 'GKA51lWQ6iwJ',
    'zddoxpdb@rambler.ru': 'K4vzzpgFiwap',
    'vjvzv8jva5@rambler.ru': 'owrR631g92is',
    'aq7dp9qonm9ib2@rambler.ru': 'Q9aFpqr1lDrn',
    'c2h5tj9rfjadv@rambler.ru': '3mxuqC0nMC27',
    'uu8f1ms3as0v5@rambler.ru': 'xLHdVwcIEZyH',
    'nwaqhmjikl@rambler.ru': 'bDcCB6XuRdrG',
    '8kgtgwq7tf9@rambler.ru': '9vo5f1IfVkax',
    'b6mmfqz1q2@rambler.ru': '9QrQbSLD5Dz8',
    'bzcdwysf32ut6s9@rambler.ru': 'rRrO0Se2PeaX',

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'support@telegram.org']


def print_logo():
    print(""" 
                               CLIENT     FOR     ooyessancez
         _   _ _   _           ______                      _     _____                       
        | \ | | | | |          | ___ \                    | |   /  ___|                      
        |  \| | | | |  ______  | |_/ /___ _ __   ___  _ __| |_  \ `--. _ __   __ _ _ __ ___  
        | . ` | | | | |______| |    // _ \ '_ \ / _ \| '__| __|  `--. \ '_ \ / _` | '_ ` _ \ 
        | |\  | |_| |          | |\ \  __/ |_) | (_) | |  | |_  /\__/ / |_) | (_| | | | | | |
        \_| \_/\___/           \_| \_\___| .__/ \___/|_|   \__| \____/| .__/ \__,_|_| |_| |_|
                                         | |                          | |                    
                                         |_|                          |_|                    

        """)


def print_menu():
    print("\033[92mМеню:\033[0m")
    print("[ 1 ] Snos аккаунта")
    print("[ 2 ] Snos канала")
    print("[ 3 ] Меню")
    print("[ 4 ] Prоверка работоспособности почты")

def send_email(receiver, sender_email, sender_password, subject, body):
    for sender_email, sender_password in senders.items():
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.rambler.ru', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)
            server.quit()
            return True
        except Exception as e:
            continue
    return False


def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0

    while sent_emails < total_emails:
        print_logo()
        print_menu()
        choice = input("\nВыбор: ")

        if choice == "1":
            print("\nВыберите тип жалобы:")
            print("\n[ 1.1 ] Обычный snos")
            print("[ 1.2 ] snos сеsсий")
            complaint_choice = input("Ваш выбор: ")

            if complaint_choice == "1.1":
                print("\nВведите причину, юзернейм, telegram ID, затем ссылки на канал/чат и на нарушение")
                reason = input("\nПричина: ")
                username = input("Юзернейм: ")
                telegram_ID = input("Telegram ID: ")
                chat_link = input("\n\nСсылка на чат: ")
                violation_chat_link = input("\nСсылка на нарушение: ")

                complaint_texts = {
                    "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(),
                                                               telegram_ID=telegram_ID.strip(),
                                                               chat_link=chat_link.strip(),
                                                               violation_chat_link=violation_chat_link.strip())
                        send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram аккаунт",
                                   complaint_body)
                        print(f"\n\n[ Удачно ] Жалоба отправлена! | {receiver_email} от {sender_email}!")
                        sent_emails += 1

            elif complaint_choice == "1.2":
                print("\nВведите юзернейм и Telegram ID")
                account_username = input("\nUsername: ")
                Telegram_account_ID = input("Telegram ID: ")

                complaint_texts = {
                    "1.2": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {account_username}, а мой айди, если злоумышленник поменял юзернейм — {Telegram_account_ID}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(account_username=account_username.strip(),
                                                               Telegram_account_ID=Telegram_account_ID.strip())
                        send_email(receiver_email, sender_email, sender_password, "Я утерял свой телеграм-аккаунт",
                                   complaint_body)
                        print(f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email} от {sender_email}!")

        elif choice == "2":
            print("\nВыберите тип жалобы:")
            print("\n\n[ 8 ] Личные данные")
            print("[ 9 ] Для прайсов")
            print("[ 10 ] Для геймов")
            print("[ 11 ] Детское питание")
            print("[ 12 ] Мошенничество")
            print("[ 13 ] Продажа вирт номеров")
            print("[ 14 ] Расчлененка")
            print("[ 15 ] Живодерство")
            complaint_type = input("\nВыбор: ")

            complaint_types = {
                "8": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются личные данные невинных людей. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform"],
                "9": [
                    "Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{violation_link} Просьба заблокировать данный канал.",
                    "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel."],
                "10": [
                    "Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance",
                    "Здравствуйте, уважаемая поддержка Telegram! Пожалуйста, заблокируйте канал {channel_link}. В этом канале угрожают расстрелом детей в школах и совершением террористических актов, вы можете увидеть это здесь {violation_link}. Заранее спасибо."],
                "11": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуется порнография с несовершеннолетними детьми. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel"],
                "12": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются посты с целью обмана и мошенничества. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform."],
                "13": [
                    "Здравствуйте, поддержка telegram. Я бы хотел пожаловаться на телеграм канал продающий виртуальные номера, насколько я знаю это запрещено правилами вашей площадки. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link} . Спасибо что очищаете свою площадку от подобных каналов!",
                    "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!"],
                "14": [
                    "Доброго времени суток, уважаемая поддержка. На просторах вашей платформы мне попался канал, распространяющий шок контент с убийствами людей. Ссылка на канал - {channel_link} , ссылка на нарушение - {violation_link} . Просьба удалить данный канал, спасибо за внимание.",
                    "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention."],
                "15": [
                    "Здравствуйте, уважаемая поддержка. На вашей платформе я нашел канал который выкладывает жестокое обращение с животными. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link}. Спасибо за то что делаете телеграм чище.",
                    "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you"],

            }

            if complaint_type not in complaint_types:
                print("\n\n[ Error ] Некорректный выбор.")
            else:
                complaint_texts = complaint_types[complaint_type]
                channel_link = input("\nСсылка на канал: ")
                violation_link = input("Ссылка на нарушение: ")

                for sender_email, sender_password in senders.items():
                    for receiver_email in random.sample(receivers, min(2, len(receivers))):
                        complaint_body = complaint_texts[0].format(channel_link=channel_link.strip(),
                                                                   violation_link=violation_link.strip())
                        send_email(receiver_email, sender_email, sender_password, "Жалоба на канал в Telegram",
                                   complaint_body)
                        print(f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email}!")
                        sent_emails += 1
                # Отправка писем на английском
                if len(complaint_texts) > 1:
                    for sender_email, sender_password in senders.items():
                        for receiver_email in random.sample(receivers, min(2, len(receivers))):
                            complaint_body = complaint_texts[1].format(channel_link=channel_link.strip(),
                                                                       violation_link=violation_link.strip())
                            send_email(receiver_email, sender_email, sender_password,
                                       "Complaint about a channel in Telegram", complaint_body)
                            print(f"Sent to {receiver_email}!")
                            sent_emails += 1
                print("[ Удачно ] Жалоба отправлена! |")

        elif choice == "5":
            print("Укажите свою почту для проверки работоспособности почт")
            test_email = input("Ваша почта: ")
            complaint_types = {
                "Тест": ["Сейчас я отправлю на почту {test_email} письма с моих почт в качестве теста"]
            }
            successfully_sent_emails = 0  # Переменная для отслеживания успешно отправленных писем
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    for complaint_choice, complaint_texts in complaint_types.items():
                        complaint_text = complaint_texts[0]
                        complaint_body = complaint_text.format(test_email=test_email.strip())
                        if send_email(receiver_email, sender_email, sender_password, "ТЕСТОВОЕ ПИСЬМО LOVE DELAINS",
                                      complaint_body):
                            successfully_sent_emails += 1
                            print(f"Отправлено на {receiver_email} от {sender_email}!")
                        else:
                            print(f"Ошибка при отправке на {receiver_email} от {sender_email}!")
            print(f"Успешно отправлено {successfully_sent_emails} писем.")


def check_access_code():
    user_input = input("Введите код доступа: ")
    if user_input in access_codes:
        print("Код доступа верный. Программа запущена.")
        return True
    else:
        print("Неверный код доступа. Программа завершает работу.")
        return False


if __name__ == "__main__":
    if check_access_code():
        handle_complaint(senders, receivers)
