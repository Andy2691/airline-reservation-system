from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str ="flights"
    DB_USER: str  ="test"
    DB_HOST: str ="localhost"
    DB_PASSWORD: str ="test"
    POOL: int = 1
    MAX_POOL: int = 2

    API_PREFIX: str = "/buscarVuelos"
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Buscar Vuelos"
    DESCRIPTION: str = "Restful API - BUSCAR VUELOS"


settings = Settings()