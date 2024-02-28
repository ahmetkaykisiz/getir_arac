from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models


def get_items(db: Session, request):
    filters = [
        models.Driver.created_at >= request.startDate if request.startDate else True,
        models.Driver.created_at <= request.endDate if request.endDate else True,
        models.Driver.driving_score >= request.minScore if request.minScore else True,
        models.Driver.driving_score <= request.maxScore if request.maxScore else True,
    ]
    combined_filters = and_(*filters)

    query = db.query(models.Driver)

    query = query.filter(combined_filters)
    return query

