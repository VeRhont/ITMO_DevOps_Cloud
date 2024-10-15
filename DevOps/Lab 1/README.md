# Отчёт по лабораторной работе №1

## Задание
- [x] Nginx должен работать по https c сертификатом
- [x] Настроить принудительное перенаправление HTTP-запросов (порт 80) на HTTPS (порт 443) для обеспечения безопасного соединения.
- [x] Использовать alias для создания псевдонимов путей к файлам или каталогам на сервере.
- [x] Настроить виртуальные хосты для обслуживания нескольких доменных имен на одном сервере.

---

### 1. Установка Nginx

Для начала установим Nginx с помощью команды `sudo apt-get install nginx`

![Installation of Nginx](media/nginx_installation.png)

Теперь узнаем свой ip адрес с помощью команды `ip addr`

![IP](media/ip_addr.png)

Вводим наш айпишник в строку браузера и пробуем подключиться к серверу. Nginx работает, так что можно двигаться дальше

![Welcome to Nginx](media/welcome_to_nginx.png)

---

### 2. Настройка Nginx

Перейдём в директорию `/var/www`. В ней будут храниться странички наших тестовых сайтов. Теперь создадим 2 новых папки с именами `test_site_1` и `test_site_2` и добавим в них HTML файлы c hello world

![test_site_1](media/mkdir.png)

Самое время написать конфиги. Перейдём в директорию `/etc/nginx/sites-available` и создадим там 2 файла с конфигурациями `test_site_1` и `test_site_2`

![test_site_1_conf](media/test_site_1_conf.png)

![test_site_2_conf](media/test_site_2_conf.png)

Чтобы Nginx мог обслуживать наши сайты, нужно создать символические ссылки на эти конфиги в `/etc/nginx/sites-enabled/`

![символические_ссылки](media/Символические_ссылки.png)

Запускаем ... И ничего не работает, страницы не найдены. Нужно добавить хосты. В файле `hosts` пропишем адреса наших сайтов

![хосты](media/add_ip.png)

Теперь перезагрузим Nginx командой `sudo service nginx restart` и попробуем подключиться вновь

![hello_world_1](media/hello_world_1.png)

![hello_world_2](media/hello_world_2.png)

Как видим, всё работает, но подключение небезопасно, так как мы используем протокол HTTP, а не HTTPS. Нужно это исправлять

---

### 3. Настройка HTTPS подключения

Чтобы сгенерировать SSL сертификат, нам понадобится openssl. Установим его
![ssl_installation](media/ssl_installation.png)

Теперь сгенерируем сам сертификат
![Certificate](media/certificate_generation.png)

Перепишем наши старые конфиги, добавив в них перенаправление с порта 80 на порт 443 
![new test_site_1 conf](media/new_test_site_2.png)
![new test_site_2 conf](media/new_test_site_1.png)

Попробуем подключиться. Браузер выдаёт предупреждение. Не обращаем внимания и подключаемся
![new test_site_1 conf](media/new_test_site_2.png)

Теперь HTTPS. Ура
![test_site_1 url](media/site_1_url.png)
![test_site_2 url](media/site_2_url.png)

---

### 4. Добавление alias 

![updated test site 1 conf](media/updated_test_site_1_conf.png)
![updated test site 2 conf](media/updated_test_site_2_conf.png)

![I_love_nginx](media/i_love_nginx.png)

![Bestsite](media/bestsite.png)


---

## Вывод
Все пункты из задания были выполнены. В качестве проектов были использованы простые html странички с текстом. 

##### Работу выполнил Иванов Семён
