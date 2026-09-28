# Проект 5. Async Data Aggregator

## Цель

Сервис, агрегирующий данные из нескольких внешних источников, глубокое изучение
aiohttp и сетевого программирования.

## Сценарий

Сервис получает запрос и одновременно обращается к нескольким внешним API.

Например, `GET /products/{id}/prices` должен запросить несколько поставщиков и
вернуть объединенный результат.

Provider A отвечает за 100 ms, Provider B — за 300 ms, Provider C зависает. API
не должен ждать Provider C бесконечно и должен уметь вернуть частичный
результат.

## Что реализовать

- concurrent HTTP requests;
- connection pooling;
- timeout;
- retry с backoff;
- semaphore;
- rate limiting;
- circuit breaker;
- обработку частичного отказа;
- кеширование;
- нормализацию разных форматов JSON;
- генераторы для потоковой обработки больших наборов данных.

## Дополнительное упражнение

Получить HTML-страницу, извлечь несколько полей через BeautifulSoup и
преобразовать их в структурированный JSON.

## Стек

FastAPI · aiohttp · asyncio · PostgreSQL · Redis · SQLAlchemy · BeautifulSoup ·
pytest · Docker Compose
