# Проект 2. Personal Finance API

## Цель

Backend для учета личных финансов, глубокая практика PostgreSQL, ORM, raw SQL
и оптимизации запросов.

## Сущности

User, Account, Category, Transaction, Budget, RecurringTransaction

## Возможности

- создание счетов;
- доходы и расходы;
- категории;
- переводы между счетами;
- месячные бюджеты;
- фильтрация операций;
- пагинация;
- статистика по месяцам;
- статистика по категориям;
- cash flow;
- сравнение расходов с предыдущим месяцем.

## Что обязательно реализовать

- часть запросов через SQLAlchemy ORM;
- сложную аналитику через raw SQL;
- CTE;
- aggregation;
- window functions;
- транзакции;
- constraints;
- индексы;
- `EXPLAIN ANALYZE`;
- намеренно создать N+1, обнаружить и исправить;
- кеширование тяжелой статистики в Redis;
- миграции;
- тесты БД.

## Права доступа к БД

Отдельным скриптом, не через ORM, создать в PostgreSQL роли `readonly` и
`readwrite`, раздать права через `GRANT`/`REVOKE` на таблицы проекта и
продемонстрировать разницу. Под `readonly` запрос на `UPDATE` должен падать.

## Стек

FastAPI · PostgreSQL · SQLAlchemy 2.x · asyncpg · Raw SQL · Alembic · Redis ·
pytest · Docker Compose
