from fastapi import FastAPI

from app.endpoints.api_routers import router
from app.db.base_class import Base
from app.db.session import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)