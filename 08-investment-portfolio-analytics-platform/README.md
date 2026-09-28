# Проект 8. Investment / Portfolio Analytics Platform

## Цель

Финальный большой проект, объединяющий навыки курса. Сервис должен быть
достаточно полезным, чтобы его можно было развивать после окончания обучения.

## Сущности

User, Portfolio, Account, Asset, Transaction, Position, Price, Dividend

## API

- создание портфеля;
- добавление сделок;
- текущие позиции;
- история стоимости портфеля;
- доходность;
- статистика;
- импорт котировок;
- фоновые обновления данных.

## Аналитика

- P&L;
- ROI;
- CAGR;
- volatility;
- Sharpe ratio;
- Sortino ratio;
- maximum drawdown.

## Архитектура

Первую версию нужно реализовать как modular monolith, а не сразу как набор
микросервисов.

Модули:

- auth;
- portfolio;
- transactions;
- market data;
- analytics;
- notifications.

Отдельный ingestion-компонент должен асинхронно получать данные из внешнего API.

После рабочей версии modular monolith дополнительным заданием нужно выделить
один модуль, например `notification-service`, в отдельный сервис.

## Что добавить

- Redis cache;
- background jobs;
- RabbitMQ;
- PostgreSQL;
- raw SQL для тяжелой аналитики;
- ORM для обычных CRUD-операций;
- idempotency;
- audit/logging;
- metrics;
- CI/CD;
- production deployment.

## Стек

FastAPI · aiohttp · PostgreSQL · SQLAlchemy · Raw SQL · Redis · RabbitMQ ·
Celery · Alembic · Docker Compose · Nginx · pytest · GitHub Actions ·
Prometheus · Grafana
