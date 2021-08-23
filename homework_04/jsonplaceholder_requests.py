"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from dataclasses import dataclass
from typing import List

from loguru import logger

from aiohttp import ClientSession


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users" 
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class Service:
    name: str
    url: str
    fields: List[str]


async def fetch_json(service: Service) -> dict:
    async with ClientSession() as session:
        result = await session.get(service.url)

    result = await result.json()
    result = {key: value for key, value in result.items()
              if key in service.fields}

    return result
        

async def get_data(
    requests_num: int,
    url: str,
    fields: List[str],
    name: str,
    timeout: int = 20,
) -> List[dict]:

    services = []
    for i in range(1, requests_num + 1):
        services.append(
            Service(
                f"{name}_{i}",
                f"{url}/{i}", 
                fields,
            )
        )

    done, pending = await asyncio.wait(
        set(asyncio.create_task(fetch_json(service)) for service in services),
        timeout=timeout,
    )

    for task in pending:
        task.cancel()

    results = [task.result() for task in done]
    return results
    

async def get_users_data(requests_num: int = 10) -> List[dict]:
    return await get_data(
        requests_num=requests_num, 
        url=USERS_DATA_URL,
        fields=['name', 'username', 'email'],
        name="user"
    )

async def get_posts_data(requests_num: int = 40) -> List[dict]:
    return await get_data(
        requests_num=requests_num, 
        url=POSTS_DATA_URL,
        fields=['userId', 'title', 'body'],
        name="post"
    )


async def main_async():
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_users_data(),
        get_posts_data(),
    )
    logger.info("\nFetch users data len: {}", len(users_data))
    logger.info("\nFetch posts data len: {}", len(posts_data))
    return users_data, posts_data
    

def main():
    users_data, posts_data = asyncio.run(main_async())
    

if __name__ == '__main__':
    main()
