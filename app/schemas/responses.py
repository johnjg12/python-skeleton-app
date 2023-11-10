from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import TypeVar, Generic, List, Optional

# Type variable for generic responses
DataT = TypeVar('DataT')


# Base API response model
class APIResponse(GenericModel, Generic[DataT]):
    data: Optional[DataT] = None
    errors: Optional[List[str]] = None

    class Config:
        # Exclude None values from the serialized output
        exclude_none = True


# Success response for a single object
class SuccessResponse(APIResponse, Generic[DataT]):
    pass


# Paging model
class Paging(BaseModel):
    page: int
    size: int
    total_pages: int
    total_items: int


# Success response for a list of objects with paging
class ListSuccessResponse(APIResponse, Generic[DataT]):
    data: List[DataT]
    paging: Optional[Paging] = None

    def has_paging(self) -> bool:
        return True


# Base error response with default status code 500
class ErrorResponse(APIResponse):
    status_code: int = 500

    @classmethod
    def create_error(cls, errors: Optional[List[str]] = None):
        if errors is None:
            errors = ["An internal server error occurred"]
        return cls(errors=errors)


class UnauthorizedErrorResponse(ErrorResponse):
    status_code: int = 401

    @classmethod
    def unauthorized_error(cls, errors: Optional[List[str]] = None):
        if errors is None:
            errors = ["Could not validate credentials"]
        return cls(errors=errors)
