"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from datetime import datetime
from typing import List

from loguru import logger

from models import Base, engine, User, Post, Session
from jsonplaceholder_requests import get_posts_data, get_users_data


async def add_users_and_posts_to_db():
    # upload data
    logger.info("Waiting for uploading data ...")

    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_users_data(requests_num=10),
        get_posts_data(requests_num=100),
    )

    logger.info("DONE")

    # update database
    async with Session() as session:
        async with session.begin():
            # add users
            session.add_all(
                list(
                    User(
                        name = d['name'], 
                        username = d['username'],
                        email = d['email']
                    )
                    for d in users_data
                )
            )

    async with Session() as session:
        async with session.begin():
            # add posts
            session.add_all(
                list(
                    Post(
                        title = d['title'], 
                        body = d['body'],
                        user_id = d['userId']
                    )
                    for d in posts_data
                )
            )


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        

async def async_main():
    await create_tables()
    await add_users_and_posts_to_db()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
