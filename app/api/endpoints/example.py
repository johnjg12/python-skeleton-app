import json
from datetime import datetime
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.core.utils import CustomJSONEncoder
from app.schemas.example import HelloWorldResponse, ExampleListResponse, ExampleItem
from app.schemas.responses import ErrorResponse, Paging

router = APIRouter()


@router.get("/hello_world", response_model=HelloWorldResponse)
async def hello_world():
    hello_response = HelloWorldResponse(data="Hello World from my Python API!")
    return JSONResponse(content=hello_response.dict(exclude_none=True))


@router.get("/list", response_model=ExampleListResponse)
async def example_list():
    # Example data with ExampleItem objects
    data = [
        ExampleItem(id=1, name="Item 1", created_at=datetime.now(), updated_at=datetime.now()),
        ExampleItem(id=2, name="Item 2", created_at=datetime.now(), updated_at=datetime.now()),
    ]
    paging = Paging(page=1, size=len(data), total_pages=1, total_items=len(data))
    list_response = ExampleListResponse(data=data, paging=paging)

    # Serialize the response using the custom JSON encoder
    json_response = json.dumps(list_response.dict(exclude_none=True), cls=CustomJSONEncoder)
    return JSONResponse(content=json.loads(json_response))


@router.get("/error", response_model=ErrorResponse)
async def example_error():
    error_response = ErrorResponse(errors=["An error occurred"])
    return JSONResponse(content=error_response.dict(exclude_none=True), status_code=400)
