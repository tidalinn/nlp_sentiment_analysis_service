import sqlite3

from src.constants import PATH_DATABASE
from src.models import ReviewIn, ReviewOut
from src.utils.logger import LOGGER


def init_db():
    with sqlite3.connect(PATH_DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(  # noqa: WPS462
            """
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    sentiment TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );
            """
        )
        connection.commit()

        LOGGER.info('Initialized table reviews')


def add_review(review: ReviewIn, sentiment: str, created_at: str) -> int:
    with sqlite3.connect(PATH_DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)',
            (review.text, sentiment, created_at)
        )
        review_id = cursor.lastrowid
        connection.commit()

        LOGGER.info(
            f'Added review id {review_id} '
            f'with text {review.text} and '
            f'sentiment {sentiment} '
            f'created at {created_at}'
        )

        return review_id


def get_reviews(sentiment: str) -> list[ReviewOut]:
    with sqlite3.connect(PATH_DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT id, text, sentiment, created_at FROM reviews WHERE sentiment=?',
            (sentiment,)
        )
        reviews = cursor.fetchall()

        LOGGER.info(f'Selected reviews with {sentiment} sentiment')

        return reviews
