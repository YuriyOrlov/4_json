# Prettify JSON

Простой скрипт для качественного вывода на экран терминала(консоли) файла в формате JSON.

---------------------------------------------------------

Simple script for good visualisation of file in JSON format.

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

    {   'Cells': {   'Address': 'Борисовский проезд, дом 40А',
                     'AdmArea': 'Южный административный округ',
                     'ClarificationOfWorkingHours': None,
                     'District': 'район Орехово-Борисово Северное',
                     'IsNetObject': 'нет',
                     'Name': 'Разливные напитки',
                     'OperatingCompany': None,
                     'PublicPhone': [{'PublicPhone': '(926) 281-82-60'}],
                     'TypeService': 'реализация продовольственных товаров',
                     'WorkingHours': [   {'DayOfWeek': 'понедельник', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'вторник', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'среда', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'четверг', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'пятница', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'суббота', 'Hours': '10:00-21:00'},
                                         {'DayOfWeek': 'воскресенье', 'Hours': '10:00-21:00'}],
                     'geoData': {'coordinates': [37.72775243734561, 55.61668660260342], 'type': 'Point'},
                     'global_id': 171714979},
        'Id': '4af7d0bb-be94-40fa-aaaa-b32ebdddc967',
        'Number': 812}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
