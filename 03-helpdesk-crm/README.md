# Проект 3. Helpdesk / CRM

## Цель

Реальная административная система, изучение Django, Django ORM и DRF.

## Сущности

User, Company, Customer, Ticket, Comment, Attachment, Tag, Status, Priority

## Роли

- клиент;
- оператор;
- администратор.

## Возможности

- создание заявки;
- назначение исполнителя;
- изменение статуса и приоритета;
- комментарии;
- вложения;
- теги;
- поиск;
- фильтрация;
- пагинация;
- история изменений;
- permissions;
- authentication.

## Django Admin

Django Admin должен позволять полноценно управлять системой.

## Middleware

Собственный middleware должен:

- генерировать `request_id`;
- измерять время запроса;
- записывать данные в лог.

## Audit log

Нужно хранить историю изменений в формате: `кто -> когда -> что изменил`.

## Стек

Django · Django REST Framework · Django ORM · PostgreSQL · Redis cache ·
pytest / pytest-django · Docker Compose · Nginx на этапе deployment
