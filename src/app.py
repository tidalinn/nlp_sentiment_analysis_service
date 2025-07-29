from fastapi import FastAPI

from src.configs import AppConfig
from src.constants import PATH_CONFIGS
from src.core import AppContainer
from src.database.sqlite import init_db
from src.routes import review
from src.utils.logger import LOGGER


def create_app() -> FastAPI:
    config = AppConfig.from_yaml(PATH_CONFIGS / 'app.yml')
    init_db()

    container = AppContainer(config=config)
    container.wire([review])

    app = FastAPI()
    app.include_router(review.router)
    LOGGER.info('Created app')

    return app
