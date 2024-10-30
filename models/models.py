from datetime import datetime, UTC

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON, Boolean

# Специальная переменная
metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    # nullable говорит о том, что этот параметр не может быть пустой
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_on", TIMESTAMP(timezone=True), nullable=False, default=datetime.now(UTC)),
    # ForeignKey как ссылка на другую таблицу
    # + более понятная логика связи таблиц
    # + нельзя использовать не существующие данные в таблицу (консистентность данных)
    # + нельзя просто так удалить таблицу, так как между ними есть связь
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)
