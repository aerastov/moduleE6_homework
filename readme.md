# DjangoChatServer
### Итоговое задание по модулю Е6
Проект состоит из клиента на JavaScript и бэкенда на Django Rest Framework, обмен информацией через WebSocket.  

Реализован базовый мессенжер со следующими функциями:  
1. Отправка и получение сообщений;
2. Создание, редактирование и удаление групповых чатов и переписка в них (управление чатами по REST API,  
а переписка так же, как в обычных чатах, но с использованием на сервере идеологии «комнат»);
3. Редактирование личной информации пользователя (имя и аватар);
4. Просмотр списка других пользователей с переходом на отправку им сообщений.


Для запуска сервера необходим IDE (я использую PyCharm), в котором установить фреймворк Django  
и следующие библиотеки:  
pip install django==3.2  
pip install djangorestframework==3.13.1  
pip install django-cors-headers==3.11.0  
pip install easy-thumbnails==2.8.1  
pip install channels==3.0.3  

Или установить все нужные библиотеки командой:  
pip install -r requirements.txt  

Запуск сервера:  
python manage.py runserver  

Для запуска клиента нужно скопировать на компьютер файлы из папки "Клиент на JS"  
и запустить в браузере index.html  
Клиент проверялся в браузере Yandex
Возможно запустить в разных вкладках копии клиента и переписываться от имени разных 
пользователей в разных комнатах.


Автор проекта: Ерастов Алексей Сергеевич  
e-mail: a.erastov@gmail.com  
Группа SkillFactory: FPW-36  
Апрель 2022 г.