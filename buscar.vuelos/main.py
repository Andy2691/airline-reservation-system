from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.routes.flights import router as flights_router
from config import settings


def get_application() -> FastAPI:
    """
    The main function that the function call

    Return: The model of fastApi
    """

    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        default_response_class=ORJSONResponse,
    )

    application.include_router(flights_router)

    return application


app = get_application()