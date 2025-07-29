from src.configs import AppConfig


class SentimentAnalyser:

    def __init__(self, config: AppConfig):
        self.config = config

    def analyze(self, text: str) -> str:
        text = text.lower()

        for sentiment, vocabulary in self.config.vocabulary_simple.items():
            if any(word in text for word in vocabulary):
                return sentiment

        return 'neutral'
