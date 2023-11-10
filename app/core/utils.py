import json
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


# Custom exception handler for HTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 401:
        # Custom response for 401 Unauthorized
        return JSONResponse(
            status_code=401,
            content={"errors": ["Could not validate credentials"]}
        )
    # Default response for other HTTP exceptions
    return JSONResponse(
        status_code=exc.status_code,
        content={"errors": [exc.detail]}
    )


# Your existing endpoint and UnauthorizedErrorResponse remain the same


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
