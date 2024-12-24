# Отчёт по лабораторной работе №2*

## Задание
- [x] Написать “плохой” Docker compose файл, в котором есть не менее трех “bad practices” по их написанию
- [x] Написать “хороший” Docker compose файл, в котором эти плохие практики исправлены
- [x] В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат
- [x] После предыдущих пунктов в хорошем файле настроить сервисы так, чтобы контейнеры в рамках этого compose-проекта так же поднимались вместе, но не "видели" друг друга по сети. В отчете описать, как этого добились и кратко объяснить принцип такой изоляции

---
### 0. Установка Docker Compose

Сначала нужно установить Docker Compose на нашу машину. Для этого воспользуемся следующими командами

```
sudo apt update
sudo apt install docker-compose
```

---
### 1. Плохой Docker Compose файл

```YAML
version: '3.8'

services:
    db:
        image: mysql:latest
        environment:
            MYSQL_USER: 'admin'
            MYSQL_ROOT_PASSWORD: 1234
        ports:
            - "3306:3306"
        volumes:
            - ./app:/var/lib/mysql

    app:
        build: .
        depends_on:
            - db
        privileged: true
        volumes:
            - ./app:/app

```
Запустим командой `docker-compose up -d --build`

### Почему так делать плохо:

1. Использование тега `:latest` может привести к непредсказуемому поведению, потому что последние версии могут быть нестабильными
2. Хардкодить пароль от базы данных в код очень плохая идея с точки зрения безопасности
3. Необоснованный запуск контейнера `app` с привилегиями опасен, потому что потенциальные злоумышленники могут получить контроль над системой
4. Отсутствие healthcheck, потому что `app` зависит от `db`

---

### 2. Хороший Docker Compose файл

```YAML
version: '3.8'

services:
    db:
        image: mysql:9.1
        environment:
            - MYSQL_USER=/run/secrets/user
            - MYSQL_ROOT_PASSWORD=/run/secrets/password
        ports:
            - "3306:3306"
        volumes:
            - ./app:/var/lib/mysql
        healthcheck:
            test: ["CMD-SHELL", "isready"]
            interval: 10s
            timeout: 5s
            retries: 5
        networks:
            - db_network

    app:
        build: .
        depends_on:
          db:
            condition: service_healthy
        privileged: false
        volumes:
            - ./app:/app
        networks:
            - app_network

secrets:
    user:
        file: ./secrets/user
    password:
        file: ./secrets/password


networks:
    db_network:
        driver: bridge
    app_network:
        driver: bridge

```

### Почему так делать хорошо:

1. Указана точная версия образа. Это избавляет от неопределенного поведения
2. Пароль теперь хранится в секретах, а это безопасно
3. Контейнер лишен привелегий в целях безопасности
4. Благодаря healthcheck мы можем гарантировать, что контейнеры работают корректно

---

### 3. Изоляция контейнеров

Чтобы изолировать контейнеры, нужно поместить их в разные сети. В хорошем файле мы создали сети `db_network` и `app_network` и прописали их для каждого из контейнеров. 

---

## Вывод
Все пункты из задания были выполнены. В ходе работы были написаны плохой и хороший docker compose файлы, а также была проведена изоляция контейнеров

##### Работу выполнил Иванов Семён
