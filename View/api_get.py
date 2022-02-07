from fastapi import APIRouter,Header
from Presenter import pre_request

router = APIRouter()

# 회사 검색 (자동완성)
@router.get('/search', tags=["Search"])
async def get_auto_search_company(query: str ,x_wanted_language: str = Header(None)):
    result = pre_request.pre_get_auto_name(query,x_wanted_language)
    return result


# 회사 검색 (회사명)
@router.get('/companies/{name}', tags=["Search"])
async def get_search_company(name : str, x_wanted_language: str = Header(None)):
    result = pre_request.pre_get_language_name(name, x_wanted_language)

    return result
