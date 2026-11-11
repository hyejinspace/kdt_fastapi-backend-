from app.infrastructure.redis import get_redis_db
from redis.asyncio import Redis
from fastapi import Depends
from sqlalchemy import insert, select, update, delete, func, exists

class RedisRepository:

    # 생성자 주입
    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    # 순수 함수
    #CRUD
    async def set(self, key: str, value: str, ex: int = 3600) -> None:
        await self.redis_client.set(key, value, ex)

    async def get(self, key: str, value: str) -> str | None:
        # get은 가져오는거기때문에 리턴값이 있음
        return await self.redis_client.get(key)

    #있는지 없는지 찾는거기때문에 bool타입
    async def exists(self, key: str) -> bool:
        result = await self.redis_client.exists(key)
        return result > 0

    async def delete(self, key: str):
        await self.redis_client.delete(key)


# 주입 팩토리 메서드
def get_redis_repository(redis_client: Redis = Depends(get_redis_db)):
    return RedisRepository(redis_client)