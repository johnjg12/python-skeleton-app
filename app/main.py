import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import JSONResponse

from app.api.middleware.trackingid import TrackingIDMiddleware
from app.core.utils import http_exception_handler
from app.schemas.responses import SuccessResponse
from app.core.logger import logger
from app.api.endpoints.example import router as example_router
from app.services import env
from app.services.auth import get_api_key
from starlette.exceptions import HTTPException as StarletteHTTPException

# Set up FastAPI
app = FastAPI(
    title="Python API",
    description="A Basic Python API.",
    version="1",
)
app.add_middleware(TrackingIDMiddleware)
# Register the custom exception handler with your FastAPI app
app.add_exception_handler(StarletteHTTPException, http_exception_handler)

# Define your FastAPI routes and endpoints here
app.include_router(example_router, prefix="/example")

# Swagger customization
original_openapi = app.openapi


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = original_openapi()
    openapi_schema["servers"] = [{"url": env.get_app_url()}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Set the custom OpenAPI function
app.openapi = custom_openapi


@app.get("/", response_model=SuccessResponse)
async def root():
    logger.info(f"Anonymous accessed the root endpoint.")
    response = SuccessResponse(data={"message": "Welcome to my Python powered API!"})
    return JSONResponse(content=response.dict(exclude_none=True))


@app.get("/authenticated", response_model=SuccessResponse)
async def root_authenticated(username: str = Depends(get_api_key)):
    logger.info(f"User '{username}' accessed the root endpoint.")
    response = SuccessResponse(data={"message": f"Welcome to my Python powered API, {username}!"})
    return JSONResponse(content=response.dict(exclude_none=True))


def main():
    # Change reload=True to if you want to enable auto-reload (don't do this in production)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
