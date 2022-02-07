from fastapi import FastAPI
from View import api_post, api_get
from Model import db_check

def include_router(app):
    app.include_router(api_get.router)
    app.include_router(api_post.router)


def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_check.table_install()
app = start_application()
