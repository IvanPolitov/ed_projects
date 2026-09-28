# Проект 6. Notification Service

## Цель

Отдельный сервис уведомлений, брокеры сообщений, фоновые задачи и event-driven
подход.

## API

API принимает запрос:

- `POST /notifications`

Типы уведомлений:

- email;
- webhook;
- условный internal notification.

## Архитектура

`API -> RabbitMQ -> Worker -> Provider`

API должен быстро возвращать `202 Accepted`, не ожидая фактической отправки.

## Что реализовать

- асинхронную постановку сообщения в очередь;
- background workers;
- retry;
- exponential backoff;
- scheduled notifications;
- историю отправок;
- шаблоны сообщений;
- idempotency;
- rate limiting;
- dead-letter обработку неуспешных сообщений;
- защиту от повторной отправки одного уведомления.

## Стек

FastAPI · RabbitMQ · Celery · Redis · PostgreSQL · SQLAlchemy · Docker Compose ·
pytest
