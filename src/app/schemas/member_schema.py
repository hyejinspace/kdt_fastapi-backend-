from pydantic import BaseModel
from datetime import datetime
from app.enums.member_enum import MemberProvider
# from app.models.post_model import Post

#VO
class MemberVO(BaseModel):
    id: int
    member_email: str
    member_password: str | None = None
    member_name: str | None = None
    member_age: int | None = None
    member_profile: str | None = "/members/default.jpg"
    member_provider_id: str | None = None
    member_provider: MemberProvider
    member_created_at: datetime | None = None

    # 한 사람이 여러개 게시글을 게시할 수 있기 때문에 Post 모델이 리스트로 들어감
    # posts: list[Post] | None = None


#DTO
class MemberCreateDTO(BaseModel):
    member_email: str
    member_password: str | None = None
    member_name: str | None = None
    member_age: int | None = None
    member_profile: str | None = "/members/default.jpg"
    member_provider: MemberProvider | None = None
    #ORM -> Pydantic
    class Config:
        from_attributes = True


# 소셜로그인 DTO
class SocialMemberCreateDTO(BaseModel):
    member_email: str
    member_name: str | None = None
    member_age: int | None = None
    member_profile: str | None = "/members/default.jpg"
    member_provider: MemberProvider | None = None
    #ORM -> Pydantic
    class Config:
        from_attributes = True


# 실무에선 안들어감(?)
class MemberClaimDTO(BaseModel):
    id: int
    member_email: str
    member_provider: str
    class Config:
        from_attributes = True


# 화면에 응답을 하는 데이터 DTO -> Response 라고 함
# 실무에선 안들어감(?)
class MemberResponseDTO(BaseModel):
    id: int
    member_email: str
    member_name: str | None = None
    member_age: int | None = None
    member_profile: str | None = "/members/default.jpg"
    member_provider_id: str | None = None
    member_provider: MemberProvider
    member_created_at: datetime | None = None
    class Config:
        from_attributes = True


class MemberUpdateDTO(BaseModel):
    member_password: str | None = None
    member_name: str | None = None
    member_age: int | None = None
    member_profile: str | None = "/members/default.jpg"
    class Config:
        from_attributes = True


class MemberSummaryDTO(BaseModel):
    id: int
    member_email: str | None = None
    memer_name: str | None = None
    member_profile: str | None = "/members/default.jpg"
    class Config:
        from_attributes = True