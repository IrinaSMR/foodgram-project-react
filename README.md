## Продуктовый помощник FOODGRAM
***

![Django-app workflow](https://github.com/IrinaSMR/foodgram-project-react/actions/workflows/main.yml/badge.svg)
***

### Стек технологий:

- Python 3.7
- DRF (Django REST framework)
- Django
- Docker
- Gunicorn
- nginx
- PostgreSQL
- GIT

### Описание проекта:

FOODGRAM - социальная сеть для любителей вкусно поесть.
Делитесь своими рецептами и пробуйте готовить новые блюда!

Проект представлен онлайн-сервисом и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

В проекте используется база данных PostgreSQL. Проект запускается в трёх контейнерах (nginx, PostgreSQL и Django) (контейнер frontend используется только для подготовки файлов) через docker-compose на сервере. Образ с проектом загружается на Docker Hub.

### Возможности сервиса:

- делитесь своими рецептами;
- знакомьтесь с рецептами других пользователей;
- добавляйте рецепты в "Избранное";
- быстро создавайте список покупок, добавив рецепт в корзину;
- следите за активностью своих друзей.

### Workflow:

- tests - проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8);
- build_and_push_to_docker_hub - сборка и доставка докер-образов на Docker Hub;
- deploy - автоматический деплой проекта на боевой сервер (выполняется копирование файлов из репозитория на сервер);
- send_message - отправка уведомления о состоянии workflow в Telegram.

***
### Запуск проекта:

Клонируйте репозиторий, перейдите в него в командной строке:

```
git clone https://github.com/IrinaSMR/foodgram-project-react.git
cd foodgram-project-react
```

Создайте и активируйте виртуальное окружение, обновите pip:

```
python -m venv venv или python3 -m venv venv для Linux
source venv/Scripts/activate или source venv/bin/activate для Linux
python -m pip install --upgrade pip
```

В репозитории на GitHub добавьте данные в Settings - Secrets - Actions secrets:

```
DOCKER_USERNAME - имя пользователя в DockerHub
DOCKER_PASSWORD - пароль пользователя в DockerHub
HOST - ip-адрес сервера
USER - имя пользователя
SSH_KEY - приватный ssh-ключ (публичный должен быть на сервере)
PASSPHRASE - кодовая фраза для ssh-ключа (если использовалась при создании)
TELEGRAM_TO - id своего телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN - токен бота (получить токен можно у @BotFather, /token, имя бота)
```

При внесении любых изменений в файлы проекта после коммита и пуша:

```
git add .
git commit -m '...'
git push
```
запускается набор блока команд jobs (см. файл main.yaml), поскольку команда git push является триггером workflow проекта.
***

### Как развернуть проект на сервере:

Установите соединение с сервером:

```
ssh username@server_address
```

Проверьте статус nginx:

```
sudo service nginx status
```

Если nginx запущен, остановите его:

```
sudo systemctl stop nginx
```

Установите Docker и Docker-compose:

```
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Проверьте корректность установки Docker-compose:

```
sudo docker-compose --version
```

В файле nginx.conf в строке server_name укажите IP виртуальной машины (сервера).
Скопируйте подготовленные файлы docker-compose.yml и nginx.conf из проекта на сервер:

```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:nginx.conf
```

### После успешного деплоя:

Соберите файлы статики:

```
sudo docker-compose exec backend python manage.py collectstatic --no-input 
```

Выполните миграции:

```
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate --no-input
```

Создайте суперпользователя:

```
sudo docker-compose exec backend python manage.py createsuperuser
```

Загрузите в базу данных ингредиенты командой:

```
sudo docker-compose exec backend python manage.py load_ingredients
```
***

## Проект развернут по адресу:

http://84.201.156.75/ - главная страница

http://84.201.156.75/admin/ - админка

(Логин админа: admin@admin.com, имя admin; пароль: admin)

http://84.201.156.75/api/ - апи


## Документация API Foodgram

http://84.201.156.75/api/docs/redoc.html

## Author
- IrinaSMR
