# Асинхронный парсер документации Python
### Описание
Парсер собирает информацию о документах PEP с официальной страницы языка Python.\
Парсер выводит собранную информацию в два файла формата csv в папку results:
1. В первом файле список всех PEP: номер, название и статус.
2. Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).
### Технологии
Python 3.10\
Scrapy 2.5.1
### Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:serebrennikovalexander/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

Linux
```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

Linix
```
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

Запустить проект:

```
scrapy crawl pep
```

### Автор
Александр Серебренников