from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Ecommerce Data Platform"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str = (
        "postgresql://postgres:postgres@database:5432/ecommerce"
    )

    class Config:
        env_file = ".env"


settings = Settings()