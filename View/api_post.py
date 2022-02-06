from fastapi import APIRouter
from pydantic import BaseModel

from Presenter import pre_request

router = APIRouter()

class AddData(BaseModel):
    company_name : dict
    tags : list


# 회사 추가
@router.post('/companies', tags=["Add"])
async def post_add_company(add : AddData):
    result = pre_request.pre_post_add(add)

    return result