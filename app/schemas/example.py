from app.schemas.responses import SuccessResponse, ListSuccessResponse


# Specific response models
class HelloWorldResponse(SuccessResponse[str]):
    pass


from datetime import datetime
from pydantic import BaseModel


# Specific object schema
class ExampleItem(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


class ExampleListResponse(ListSuccessResponse[ExampleItem]):
    pass
