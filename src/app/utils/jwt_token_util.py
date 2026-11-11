import os
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from app.schemas.member_schema import MemberClaimDTO

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# 1. Access_token 생성하는 함수
def generate_access_token(member_claims: MemberClaimDTO) -> str:
    # DTO -> dict
    claims = member_claims.model_dump()

    # eccess_token: 1~5분 (일회용, 실무는 3분정도 추천 but 우리는 개발단계이니 24시간으로 둘거임)
    expire = datetime.now(timezone.utc) + timedelta(minutes=1)
    access_token = jwt.encode(
        {
            **claims,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return access_token

# 2. refresh_token 생성하는 함수
def generate_refresh_token(member_claims: MemberClaimDTO) -> str:
    # DTO -> dict
    claims = member_claims.model_dump()

    expire = datetime.now(timezone.utc) + timedelta(days=30)
    refresh_token = jwt.encode(
        {
            **claims,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return refresh_token

# 3. token_parsing 함수 (token -> user info)
def parse_token(token: str) -> MemberClaimDTO:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    member_id = payload["id"]
    member_email = payload["member_email"]
    member_provider = payload["member_provider"]

    # MemberClaimDTO.model_validate(payload)

    return MemberClaimDTO(
        id=member_id,
        member_email=member_email,
        member_provider=member_provider
    )

# 4. refresh_token을 이용해서 access_token 재발급
def reissue_access_token(refresh_token: str) -> str:
    claims = parse_token(refresh_token)
    new_access_token = generate_access_token(claims)
    return new_access_token