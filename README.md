# Prettify JSON

Простой скрипт для качественного вывода на экран терминала(консоли) файла в формате JSON.

---------------------------------------------------------

Simple script for good visualisation of file in JSON format.

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

{
        "Cells": {
            "Address": "улица Академика Королёва, дом 3",
            "AdmArea": "Северо-Восточный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "Останкинский район",
            "IsNetObject": "да",
            "Name": "Магазин «Отдохни»",
            "OperatingCompany": "Отдохни",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 424-95-15"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:00-23:00"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:00-23:00"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.63310099917504,
                    55.820912000154024
                ],
                "type": "Point"
            },
            "global_id": 171714826
        },
        "Id": "a5d9874a-600e-400d-8512-a8215599ecaa",
        "Number": 811
    },

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
