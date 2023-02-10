from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://postgres:reuza1908@localhost:5432/startupAlcantara'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    AUTH_COOKIE_NAME: str = 'guniversity'
    SALTY: str = 'QaPR14SfNkzBtRCjJCFVTtFYljcunxXI-g4hP9g2IhYgrEmiBtzBqoeAPGFEwcyV56d5nwR52zomRL7JhiR3QA'

    class Config:
        case_sensitive = True



settings: Settings = Settings()
