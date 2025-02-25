from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.routes.users import router as users_routes
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

    application.include_router(users_routes)

    return application


app = get_application()
