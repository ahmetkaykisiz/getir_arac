from fastapi import HTTPException
from fastapi.logger import logger
from sqlalchemy.orm import Session
from utils.database import SessionLocal, engine
from utils import util_models
from pydantic import ValidationError

from fastapi import Depends, FastAPI

from utils.pagination import paginate
from utils.schemas import (DriverRequest)
from utils import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/arac_api/driver_list/")
async def read_items(
        request: DriverRequest,
        db: Session = Depends(get_db),
):
    try:
        items_query = util_models.get_items(db, request)
        return paginate(items_query, request.offset, request.limit)

    except ValidationError as exc:
        logger.exception(f"['get ValidationError - /driver_list'] Error: {str(exc)}, {repr(exc.errors()[0]['type'])}")
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as e:
        logger.exception(f"['get - /driver_list'] Error: {str(e)}")

        raise HTTPException(status_code=500, detail=str(e))
