from sqlalchemy.orm import Session
from sqlalchemy import and_

from arac_api.utils import models
from arac_api.utils.models import Driver


def get_items(db: Session, request):
    filters = [
        Driver.created_at >= request.startDate if request.startDate else True,
        Driver.created_at <= request.endDate if request.endDate else True,
        Driver.driving_score >= request.minScore if request.minScore else True,
        Driver.driving_score <= request.maxScore if request.maxScore else True,
    ]
    combined_filters = and_(*filters)

    query = db.query(models.Driver)

    query = query.filter(combined_filters)
    return query

