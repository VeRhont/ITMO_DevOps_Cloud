# Отчёт по лабораторной работе №3

## Задание
- [x] Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD
- [x] Написать “хороший” CI/CD, в котором эти плохие практики исправлены
- [x] В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат

---

### 1. Настройка

Для начала создадим простенький проект на python с помощью которого будем обращаться к [openweathermap.org](https://openweathermap.org/) и получать данные о погоде. В директорию `.github/workflows` добавим файл `actions.yml`, в котором мы и будем описывать весь pipeline. В качестве CI/CD инструмента будем использовать GitHub Actions

---

### 2. Плохой CI/CD файл

```YAML
name: Bad pipeline

on:
  push:

jobs:
  do_everything:
    runs-on: ubuntu-latest
    steps:
      - name: setup
        uses: actions/checkout@v2

      - name: setup
        uses: actions/setup-python@v4
        with:
          python-version: 3.11.5

      - name: install
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: test
        run: |
          python test.py

      - name: execute script
        env:
          API_TOKEN: "a4819dks02881ud8194hn130021" # (токен не настоящий)
        run: python main.py

      - name: commit files
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git diff-index --quiet HEAD || (git commit -a -m "updated logs" --allow-empty)

      - name: push changes
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main
```

##### Плохие практики в этом файле:

1. В моменте `on: push` мы запускаем пайплайн на любой push в любую ветку, что может быть излишним и занимать много времени
2. Мы используем всего лишь один job `do_everything`. Это затрудняет процесс отладки, к тому же выполнение одного большой pipeline займёт больше времени
3. Шагам даны неинформативные и повторяющиеся имена, такие как `setup`. Это затруднит отладку, и нам будет сложнее понять в каком месте произошла ошибка
4. Секрет `API_TOKEN` хранится прямо в коде. Это очень небезопасно, ведь любой сможет его узнать 
5. Использование старых версий у `actions/checkout@v2`, `actions/setup-python@v4`, `ad-m/github-push-action@v0.6.0`
6. Захардкодена версия python

---

### 3. Хороший CI/CD файл

```YAML
name: Good pipeline

on:
  push:
    branches:
      [main]

jobs:
  build:
    strategy:
      matrix:
        python-version: [ 3.11.5 ]
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo content
        uses: actions/checkout@v4

      - name: setup python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: install python packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: execute script
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
        run: python main.py

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: checkout repo content
        uses: actions/checkout@v4
      - name: run tests
        run: |
          python test.py

  deploy:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - name: checkout repo content
        uses: actions/checkout@v4

      - name: commit files
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git diff-index --quiet HEAD || (git commit -a -m "updated logs" --allow-empty)

      - name: push changes
        uses: ad-m/github-push-action@v0.8.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main
```

##### Исправление плохих практик

1. Чётко указано, когда запускать пайплайн
2. Весь pipeline разбит на 3 джоба: `build`, `test`, `deploy`
3. Всем шагам даны понятные и уникальные имена
4. Теперь секрет хранится безопасно
5. Использование новых версий у `actions/checkout@v4`, `actions/setup-python@v5`, `ad-m/github-push-action@v0.8.0`
6. Использована strategy: `matrix: python-version [ 3.11.5 ]`

---

## Вывод
Все пункты из задания были выполнены. В ходе работы были написаны CI/CD файл с использованием плохих практик, а также исправленный CI/CD файл с использованием лучших практик

##### Работу выполнил Иванов Семён
