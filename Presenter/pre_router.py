from fastapi import APIRouter

from View import api_get, api_post

api_router = APIRouter

api_router.include_router(api_get.router, tags=["get"])
api_router.include_router(api_post.router, tags=["post"])