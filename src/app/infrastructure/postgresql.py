# FastAPI가 PostgreSQL 데이터베이스를 사용할 수 있도록 준비하는 파일

# 환경변수 읽기 등 운영체제 관련 기능
import os
# .env 파일의 값을 불러오는 기능
from dotenv import load_dotenv
# 비동기 DB 엔진 생성,DB 세션을 만드는 공장, 비동기 DB 세션의 타입
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# SQLAlchemy 모델의 부모 클래스
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

POSTGRESQL_DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")

# 1. 비동기 전영 DB 엔진 생성
engine = create_async_engine(
    POSTGRESQL_DATABASE_URL, echo=True
)
# echo=True : SQLAlchemy가 실행하는 SQL문을 콘솔에 출력하라는 뜻



# 2. 비동기 세션 생성기 
# AsyncSessionLocal이라는 이름으로 DB 세션을 만들어 주는 공장을 만든다.
AsyncSessionLocal = async_sessionmaker(
    # 어떤 DB 엔진
    bind=engine,
    # 어떤 종류의 세션을 만들지 지정
    class_=AsyncSession,
    # 커밋 후에도 이미 가져온 객체의 속성을 만료시키지 않음
    expire_on_commit=False # 비동기 설정 필수값
)

# 3. Model은 반드시 Base를 상속받아서 설계해야 ORM이 관리해준다.
class Base(DeclarativeBase):
    pass 

# ※ 4. FastAPI 비동기 의존성 주입(Dependency Injection)을 처리하는 함수
async def get_postgresql_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db

        finally:
            await db.close()


