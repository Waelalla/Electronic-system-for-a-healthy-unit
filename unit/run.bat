@echo off
if %1 == serve  py manage.py runserver
if %1 == migrations  py manage.py makemigrations
if %1 == migrate  py manage.py migrate