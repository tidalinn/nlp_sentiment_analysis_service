from datetime import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from src.core import AppContainer
from src.core.sentiment_analyser import SentimentAnalyser
from src.database import sqlite
from src.models import ReviewIn, ReviewOut

router = APIRouter(prefix='/reviews', tags=['sentiment'])


@router.post('/', response_model=ReviewOut)
@inject
def add_review(
    review: ReviewIn,
    service: SentimentAnalyser = Depends(Provide[AppContainer.sentiment_analyser])  # noqa: WPS404
):
    sentiment = service.analyze(review.text)
    created_at = datetime.utcnow().isoformat()
    review_id = sqlite.add_review(review, sentiment, created_at)

    return ReviewOut(
        id=review_id,
        text=review.text,
        sentiment=sentiment,
        created_at=created_at
    )


@router.get('', response_model=list[ReviewOut])
def get_reviews(sentiment: str = Query('negative')):  # noqa: WPS404
    reviews = sqlite.get_reviews(sentiment)

    return [
        ReviewOut(
            id=review[0],
            text=review[1],
            sentiment=review[2],
            created_at=review[3]
        )
        for review in reviews
    ]
