import os

from fastapi import HTTPException, Depends, status
from fastapi.security.api_key import APIKeyHeader
from typing import Dict
import json

from app.schemas.responses import UnauthorizedErrorResponse

API_KEY_NAME = "access_token"
API_KEYS_FILENAME = os.getenv('API_KEYS_JSON_PATH', "local_resources/api_keys.json")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def load_api_keys() -> Dict[str, str]:
    try:
        with open(API_KEYS_FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_api_keys(api_keys: Dict[str, str]):
    with open(API_KEYS_FILENAME, "w") as file:
        json.dump(api_keys, file, indent=4)


API_KEYS = load_api_keys()


async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header not in API_KEYS:
        # Using UnauthorizedErrorResponse instead of raising HTTPException
        error_response = UnauthorizedErrorResponse.unauthorized_error()
        raise HTTPException(
            status_code=error_response.status_code,
            detail=error_response.dict(exclude={'status_code'})  # Exclude status_code from the response body
        )
    return API_KEYS[api_key_header]
