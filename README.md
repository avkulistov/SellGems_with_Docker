# SellGems
RestFull API for SellGems

# Установка и запуск
Для работы с приложением необходим установленный Docker и docker-compose.

Сборка осуществляется в каталоге приложения запуском команды _**"docker-compose build"**_,
после чего запускается одной командой _**"docker-compose up"**_.

# URL для запросов
Загрузка .csv файлов в базу данных через POST запрос:<br>
<pre>127.0.0.1:8000/api/v1/deals/upload_file</pre>
Получение данных о 5 клиентах потративших наибольшую сумму за весь период GET запросом:<br>
<pre>127.0.0.1:8000/api/v1/deals/spent_users</pre>
Получение всех записей из базы данных:<br>
<pre>127.0.0.1:8000/api/v1/deals/all</pre>
Создание новой записи в базе данных:<br>
<pre>127.0.0.1:8000/api/v1/deals/deal/create</pre>
Изменение конкретной записи в базе:<br>
<pre>127.0.0.1:8000/api/v1/deals/deal/detail/{pk}

параметры:
pk - ключ записи в базе</pre>

