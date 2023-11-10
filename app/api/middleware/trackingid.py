import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TrackingIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        tracking_id = str(uuid.uuid4())
        logger.info(f"tracking_id={tracking_id} path={request.url.path}")
        response = await call_next(request)
        response.headers["TrackingID"] = tracking_id
        return response
