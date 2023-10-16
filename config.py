from pydantic import Field
from pydantic_settings import BaseSettings




class Settings(BaseSettings):
    DB_ENDPOINT: str = Field(env="DB_ENDPOINT")
    DB_PORT: int = Field(env="DB_PORT")
    DB_PASSWORD: str = Field(env="DB_PASSWORD")
    DB_USERNAME: str = Field(env="DB_USERNAME")
    DB_NAME: str = Field(env="DB_NAME")

    class Config:
        env_file = ".env"

settings = Settings()
