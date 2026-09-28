# Проект 1. Async Job Runner

## Цель

Создать сервис фонового выполнения пользовательских задач. Главная цель проекта
— разобраться в `asyncio`, конкурентности, HTTP и жизненном цикле фоновой
задачи.

## REST API

- `POST /jobs` — создать задачу.
- `GET /jobs/{id}` — получить состояние и результат.
- `GET /jobs` — список задач с пагинацией и фильтрацией.
- `POST /jobs/{id}/cancel` — отменить задачу.

## Статусы задач

`PENDING -> RUNNING -> COMPLETED / FAILED / CANCELLED`

## Типы задач

1. `sleep` — ожидание N секунд.
2. `http_request` — HTTP-запрос.
3. `url_check` — проверка доступности URL и времени ответа.
4. `batch_http` — конкурентная обработка списка URL.

## Что реализовать

- `asyncio.Queue`;
- несколько worker'ов;
- ограничение concurrency;
- timeout;
- cancellation;
- retry с декоратором из Pre-flight;
- graceful shutdown;
- сохранение состояния задач в PostgreSQL;
- сравнение sync / threads / processes / asyncio на отдельном benchmark;
- небольшое отдельное упражнение TCP client/server;
- генератор/итератор для последовательной выдачи задач;
- unit и integration tests.

## Стек

FastAPI · asyncio · aiohttp или httpx · PostgreSQL · SQLAlchemy 2.x async ·
asyncpg · Alembic · Pydantic · pytest · Docker Compose · Ruff · mypy

## Ограничения

На этом этапе не использовать Celery, RabbitMQ и Redis.
