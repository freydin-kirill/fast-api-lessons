from datetime import datetime, UTC

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

# Специальная переменная
metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column("id", Integer, primary_key=True),
    # nullable говорит о том, что этот параметр не может быть пустой
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_on", TIMESTAMP, nullable=False, default=datetime.now(UTC)),
    # ForeignKey как ссылка на другую таблицу
    # + более понятная логика связи таблиц
    # + нельзя использовать не существующие данные в таблицу (консистентность данных)
    # + нельзя просто так удалить таблицу, так как между ними есть связь
    Column("role_id", Integer, ForeignKey("roles.id")),
)
