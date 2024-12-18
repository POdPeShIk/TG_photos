# Описание программы 
 Программа предназначена для скачивания фотографий из космоса и последующей их отправки в Telegram- канал каждые несколько часов. 

## Установка и запуск 
Программа должна быть установлена с использованием менеджера пакетов, такого как pip. После установки запустите программу с помощью соответствующего скрипта.
Клонируйте репозиторий:
```
git clone https://github.com/POdPeShIk/TG_photos
```

## Требования 
Программа должна работать на Python и использовать библиотеку python-telegram-bot для взаимодействия с Telegram API, а также определенные версии некоторых библиотек, которые можно найти в папке requirements.
```
pip install -r requirements.txt
```

## Использование 
Программа должна принимать параметры, которые можно указать в папке .env. Указания имени канала Telegram:
```
TG_CHAT_ID=@<имя канала>
```

Указания времени (1 раз за указанное время будет отправляться фотография):
```
WAITING_TIME=<ваше время>
``` 

Токен вашего telegram бота:
```
TELEGRAM_TOKEN=<ваш токен>
```
ID отправки корабля:
```
LAUNCH_ID=<ID>
```

Api_key для скачивания фотографий с сайта SpaceX(его можно сгенерировать на сайте NASA):
```
NASA_API_KEY=<ваш апи кей>
```

Директорию откуда будет браться фото на отправление:
```
DIRECTORY=images/<директория>
```


## Примеры запуска
tg.py:
```angular2html
python send_imgs_tg.py --path images/APOD/image_apod_1.jpg
```

fetch_epic_images.py:
```angular2html
python fetch_epic_images.py --date 2023-10-2 
```

fetch_apod_images.py:
```angular2html
python fetch_apod_images.py --date 2023-10-2
```

fetch_spacex_images.py:
```angular2html
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```

main.py:
```angular2html
python main.py
```


