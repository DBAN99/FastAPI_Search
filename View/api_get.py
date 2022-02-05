from fastapi import APIRouter


router = APIRouter()

# 회사 검색 (자동완성)
@router.get('/search', tags=["Search"])
async def get_search_company(query : str):
    result = '검색'

    return result

# 회사 검색 (회사명)
@router.get('/companies', tags=["Search"])
async def get_search_company():
    result = '검색'

    return result

