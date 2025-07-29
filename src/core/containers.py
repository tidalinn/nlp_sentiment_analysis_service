from dependency_injector import containers, providers

from src.configs import AppConfig
from src.core.sentiment_analyser import SentimentAnalyser


class AppContainer(containers.DeclarativeContainer):
    config = providers.Object(AppConfig)

    sentiment_analyser = providers.Singleton(
        SentimentAnalyser,
        config=config
    )
