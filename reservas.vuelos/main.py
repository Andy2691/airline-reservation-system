from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.routes.reservations import router as reservations_router
from config import settings


def get_application() -> FastAPI:
    """
    The main function that initializes the FastAPI application.

    Return: The FastAPI instance
    """

    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Microservicio para la gestión de reservas de vuelos.",
        default_response_class=ORJSONResponse,
    )

    application.include_router(reservations_router)

    return application


app = get_application()


