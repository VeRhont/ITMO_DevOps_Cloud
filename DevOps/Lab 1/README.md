# Отчёт по лабораторной работе №1

## Задание
- [x] Nginx должен работать по https c сертификатом
- [x] Настроить принудительное перенаправление HTTP-запросов (порт 80) на HTTPS (порт 443) для обеспечения безопасного соединения.
- [x] Использовать alias для создания псевдонимов путей к файлам или каталогам на сервере.
- [x] Настроить виртуальные хосты для обслуживания нескольких доменных имен на одном сервере.

---

### 1. Установка Nginx

Для начала нужно установить Nginx
![Installation of Nginx](media/nginx_installation.png)

Теперь узнаем свой ip адрес
![IP](media/ip_addr.png)

Пробуем подключиться
![Welcome to Nginx](media/welcome_to_nginx.png)

---

### 2. Настройка Nginx

Перейдём в директорию `/var/www`

Создадим 2 новых папки, в которых будут храниться странички наших сайтов
![test_site_1](media/mkdir.png)

А теперь напишем и сами странички c hello world

Самое время написать конфиги 
![test_site_1_conf](media/test_site_1_conf.png)

![test_site_2_conf](media/test_site_2_conf.png)

Чтобы Nginx обслуживал наши сайты, нужно создать символические ссылки на файлы конфигурации `test_site_1` и `test_site_2` в `/etc/nginx/sites-enabled/`

![символические_ссылки](media/Символические_ссылки.png)

Запускаем ... И ничего не работает. Нужно добавить хосты

![DNS](media/add_ip.png)

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

![I_love_nginx](media/I_love_nginx.png)

![Bestsite](media/bestsite.png)


---

## Вывод
Все пункты из задания были выполнены. В качестве проектов были использованы простые html странички с текстом. 

##### Работу выполнил Иванов Семён
