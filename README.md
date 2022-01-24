# Webtronics test

Тестовое задание.

## Installation

Чтобы запустить проект, выполните следующие команды

```bash
cat .env.temp > .env
docker compose up --build
```

После успешного запуска сервера, выполните

```bash
docker compose exec web python manage.py migrate
```

Следующие запуски

```bash
docker compose up
```

## Docs

Документация доступна по адресу http://0.0.0.0:8000/docs/

## Admin

Чтобы воспользоваться встроенной админкой выполните

```bash
docker compose exec web python manage.py createsuperuser --noinput
```

Затем перейдите по адресу http://0.0.0.0:8000/admin/. Логин и пароль admin.

## Email hunter

Чтобы включить проверку email при регистрации пользователя, замените следующие
переменные в .env:
1. EMAIL_VERIFICATION замените на 1
2. EMAIL_HUNTER_KEY введите api_key из личного кабинета hunter.io

## Tests

Чтобы запустить тесты, воспользуйтесь командой

```bash
docker compose exec web pytest
```
