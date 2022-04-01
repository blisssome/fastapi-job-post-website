from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import Settings
from db.session import engine
from db.tables import Base
from apis.base import api_router

from apis.version1.route_general_pages import router

def include_router(app):
    app.include_router(api_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=Settings.PROJECT_NAME,
                  version=Settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

app = start_application()

