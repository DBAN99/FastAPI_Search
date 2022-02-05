from fastapi import APIRouter

router = APIRouter()

# 회사 추가
@router.post('/companies', tags=["Add"])
async def post_add_company():
    result = '추가'

    return result