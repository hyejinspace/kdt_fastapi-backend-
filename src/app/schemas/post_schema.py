from pydantic import BaseModel
from datetime import datetime
from app.schemas.member_schema import MemberSummaryDTO

# VO
class PostVO(BaseModel):
    id: int
    post_title: str
    post_content: str
    post_read_count: int
    post_updated_at: datetime | None = None
    post_created_at: datetime | None = None

    member_id: int
    # member: Member

#DTO
class PostCreateDTO(BaseModel):
    post_title: str
    post_content: str

    class Config:
        from_attributes = True

#DTO
# 응답을 처리하기위해서 담아서 처리하는거는 response 임(이름규칙) - 실무에서는 DTO라고 안드감. 그냥 response임
class PostDetailResponseDTO(BaseModel):
    id: int
    post_title: str
    post_content: str
    post_read_count: int
    post_updated_at: datetime | None = None
    post_created_at: datetime | None = None

    member: MemberSummaryDTO 

    class Config:
        from_attributes = True

#DTO
class PostListResponseDTO(BaseModel):
    id: int
    post_title: str
    post_read_count: int
    post_updated_at: datetime | None = None
    post_created_at: datetime | None = None
    member: MemberSummaryDTO 

    class Config:
        from_attributes = True


class PostUpdateDTO(BaseModel):
    post_title: str
    post_content: str

    class Config:
        from_attributes = True
