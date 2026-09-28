# Проект 7. Production Deployment

## Цель

Взять один из предыдущих сервисов и довести его до состояния, близкого к
production.

## Шаг 0: ручной deployment без Docker

Прежде чем контейнеризировать сервис, нужно задеплоить тот же сервис руками на
VPS или VM:

- uWSGI или Gunicorn/Uvicorn для FastAPI как application server;
- Nginx как reverse proxy и отдача статики;
- конфиг через `.ini` или systemd-unit, а не inline-командами.

Смысл шага — увидеть, что именно потом абстрагирует Docker.

## Контейнеры

- API;
- worker, если нужен;
- PostgreSQL;
- Redis;
- RabbitMQ, если нужен;
- Nginx.

## Что настроить

- Dockerfile;
- multi-stage build;
- Docker Compose;
- volumes;
- networks;
- healthcheck;
- environment variables;
- secrets;
- Nginx reverse proxy;
- HTTPS;
- graceful shutdown;
- structured logging.

## HTTPS

Нужно привязать домен, например бесплатный поддомен через duckdns.org, через
A-запись. Certbot должен выпустить сертификат Let's Encrypt и настроить
автопродление. Проверить автопродление командой `certbot renew --dry-run`.

Nginx должен принудительно редиректить HTTP на HTTPS, прямой HTTP-доступ должен
быть закрыт. Итог проверяется через SSL Labs, цель — рейтинг A или A-.

## Bash-автоматизация

`deploy.sh`:

- `git pull`;
- build;
- `up -d`;
- health-check по `/health`;
- откат при неудаче;
- идемпотентность;
- `set -euo pipefail`;
- логирование каждого шага.

`backup.sh`:

- `pg_dump` с датой в имени;
- ротация, хранить последние 7 копий;
- запуск через cron.

## CI/CD

Пайплайн: `push / pull request -> lint -> type check -> tests -> build Docker image`.

Добавить Ruff, mypy, pytest и GitHub Actions.

## Практика Linux

Процессы, signals, permissions, environment variables, networking, `curl`,
`ps`, `top`, `grep`, `journalctl`, базовая диагностика работающего сервиса.

## Стек

Docker · Docker Compose · Linux · Nginx · uWSGI · certbot · GitHub Actions ·
Ruff · mypy · pytest · Uvicorn / Gunicorn при необходимости
